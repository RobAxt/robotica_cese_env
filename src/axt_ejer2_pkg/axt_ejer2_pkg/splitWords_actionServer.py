import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
from rclpy.action import CancelResponse, GoalResponse
from axt_ejer2_interfaces.action import SplitWords

import time

class SplitWordsActionServer(Node):
    def __init__(self):
        super().__init__('split_words_action_server')
        
        self.action_server = ActionServer(
            self, 
            SplitWords, 
            "splitwords", 
            execute_callback = self.execute_callback, # Procesa el Goal y se fija si fue cancelado
            goal_callback    = self.goal_callback,    # Acepta o rechaza el Goal
            cancel_callback  = self.cancel_callback   # Recibe la cancelacion y la acepta
            )
        self.get_logger().info("[Inicio] SplitWords Action Server inicializado y a la espera de goals...")


    def goal_callback(self, goal_handle: ServerGoalHandle):
        text_target = goal_handle.text.strip()
        if not text_target:
            self.get_logger().warn('[GoalRechazado] Texto vacío. Se rechaza el goal.')
            return GoalResponse.REJECT
        
        num_words = len(text_target.split())
        self.get_logger().info(f'[GoalAceptado] Recibido texto con {num_words} palabras.')
        return GoalResponse.ACCEPT


    def cancel_callback(self, goal_handle: ServerGoalHandle):
        self.get_logger().info('[CancelRequest] Solicitud de cancelación recibida. Se acepta.')
        return CancelResponse.ACCEPT


    def execute_callback(self, goal_handle: ServerGoalHandle):
        self.get_logger().info('[Ejecutando] Iniciando procesamiento de SplitWords…')
        text_target = goal_handle.request.text.strip()
        words = text_target.split()

        feedback_msg = SplitWords.Feedback()
        result_msg = SplitWords.Result()

        total = len(words)
        counter = 0

        for word in words:
            # Verificar si hubo una solicitud de cancelación:
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info(f'[Cancelado] Enviando resultado parcial: {counter} palabras procesadas.')
                result_msg.total_words = counter
                return result_msg
            
            # Publicar feedback:
            feedback_msg.current_word = word
            goal_handle.publish_feedback(feedback_msg)
            counter += 1
            self.get_logger().info(f'[Feedback] "{word}" ({counter}/{total})')
            time.sleep(1.0)

        result_msg.total_words = total
        goal_handle.succeed()
        self.get_logger().info(f'[Success] Acción completada. Total de palabras: {total}')
        return result_msg


def main(args=None):
    rclpy.init(args=args)
    server_node = SplitWordsActionServer()
    try:
        rclpy.spin(server_node)
    except KeyboardInterrupt:
        pass
    finally:
        # Destruir el servidor y el nodo antes de apagar
        server_node.destroy_node()
        rclpy.try_shutdown()

if __name__ == '__main__':
    main()