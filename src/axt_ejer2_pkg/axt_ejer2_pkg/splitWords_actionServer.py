#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action import CancelResponse, GoalResponse

# Importamos el tipo de acción ahora que ya se generó:
from axt_ejer2_pkg.action import SplitWords

import time

class SplitWordsActionServer(Node):
    """
    Nodo Action Server que recibe un texto completo como goal y envía cada palabra
    como feedback a 1 Hz (una palabra por segundo), devolviendo al final la cantidad
    de palabras procesadas.
    """

    def __init__(self):
        super().__init__('split_words_action_server')

        # Creamos el ActionServer con:
        #  - self: nuestro nodo
        #  - SplitWords: el tipo de acción que definimos en SplitWords.action
        #  - 'split_words': nombre bajo el cual se publica el servidor (/split_words/...)
        #  - execute_callback: función que se ejecuta cuando aceptamos un goal
        #  - goal_callback: función para aceptar/rechazar goals entrantes
        #  - cancel_callback: función para aceptar/rechazar cancelaciones
        self._action_server = ActionServer(
            self,
            SplitWords,
            'split_words',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback
        )

        self.get_logger().info('Action Server "split_words" inicializado y a la espera de goals...')

    def goal_callback(self, goal_request):
        """
        Cada vez que llega un goal, este callback decide si lo aceptamos o no.
        goal_request.text contiene el texto enviado por el cliente.
        """
        texto_recibido = goal_request.text.strip()
        if not texto_recibido:
            self.get_logger().warn('[GoalRechazado] Texto vacío. Se rechaza el goal.')
            return GoalResponse.REJECT

        num_palabras = len(texto_recibido.split())
        self.get_logger().info(f'[GoalAceptado] Recibido texto con {num_palabras} palabras.')
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        """
        Si el cliente pide cancelar el goal en curso, este callback decide si lo acepta.
        """
        self.get_logger().info('[CancelRequest] Solicitud de cancelación recibida. Se acepta.')
        return CancelResponse.ACCEPT

    def execute_callback(self, goal_handle):
        """
        Función principal que se ejecuta tras aceptar un goal:
         1. Recupera goal_handle.request.text (el texto completo).
         2. Divide el texto en palabras con split().
         3. Publica cada palabra como feedback a 1 Hz.
         4. Permite cancelar a mitad de ejecución.
         5. Al terminar (o cancelar), marca el goal como succeeded/canceled y devuelve un Result.
        """
        self.get_logger().info('[Ejecutando] Iniciando procesamiento de SplitWords…')

        texto = goal_handle.request.text
        palabras = texto.split()  # por defecto separa por espacios en blanco

        feedback_msg = SplitWords.Feedback()
        resultado = SplitWords.Result()

        total = len(palabras)
        contador = 0

        for palabra in palabras:
            # Verificar si hubo una solicitud de cancelación:
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info(f'[Cancelado] Enviando resultado parcial: {contador} palabras procesadas.')
                resultado.total_words = contador
                return resultado

            # Publicar feedback:
            feedback_msg.current_word = palabra
            goal_handle.publish_feedback(feedback_msg)
            contador += 1
            self.get_logger().info(f'[Feedback] "{palabra}" ({contador}/{total})')
            time.sleep(1.0)  # Esperamos 1 segundo entre palabras

        # Si llegamos hasta acá, completamos todas las palabras sin ser cancelados:
        resultado.total_words = total
        goal_handle.succeed()
        self.get_logger().info(f'[Success] Acción completada. Total de palabras: {total}')
        return resultado

def main(args=None):
    rclpy.init(args=args)
    server_node = SplitWordsActionServer()
    try:
        rclpy.spin(server_node)
    except KeyboardInterrupt:
        pass
    finally:
        # Destruir el servidor y el nodo antes de apagar
        server_node._action_server.destroy()
        server_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
