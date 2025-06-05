import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.executors import ExternalShutdownException
from axt_ejer2_interfaces.action import SplitWords


class SplitWordsActionClient(Node):
    def __init__(self):
        super().__init__('split_words_action_client')
        
        self.declare_parameter('text', 'Sphinx of black quartz, judge my vow.')
        self.param_text = self.get_parameter('text').get_parameter_value().string_value

        self.action_client = ActionClient(self, SplitWords, 'splitwords')


    def sendGoal(self):
        if not self.action_client.wait_for_server(timeout_sec=5.0):
            self.get_logger().error(
                '¡Timeout! El Action Server "/splitwords" no está disponible.'
            )
            return

        goal_msg = SplitWords.Goal()
        goal_msg.text = self.param_text

        self.get_logger().info(f'[Cliente] Enviando goal con texto: "{self.param_text}"')

        send_goal_future = self.action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        send_goal_future.add_done_callback(self.goal_response_callback)


    def feedback_callback(self, feedback_msg):
        current_word = feedback_msg.feedback.current_word
        self.get_logger().info(f'[Cliente][Feedback] Palabra actual: "{current_word}"')


    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().warn('[Cliente] El servidor rechazó el goal.')
            exit()

        self.get_logger().info('[Cliente] Goal aceptado. Esperando resultado...')

        get_result_future = goal_handle.get_result_async()
        get_result_future.add_done_callback(self.get_result_callback)


    def get_result_callback(self, future):
        result = future.result().result
        status = future.result().status

        if status == 5:  # CANCELLED
            self.get_logger().info(
                f'[Cliente] Goal cancelado. Palabras procesadas hasta el momento: {result.total_words}'
            )
        elif status == 4:  # SUCCEEDED
            self.get_logger().info(
                f'[Cliente] Acción completada con éxito. Total de palabras: {result.total_words}'
            )
        else:
            self.get_logger().info(
                f'[Cliente] Goal terminado con estado {status}.'
                f'Palabras procesadas: {result.total_words}'
            )
        
        exit()


def main(args=None):
    rclpy.init(args=args)
    client_node = SplitWordsActionClient()
    client_node.sendGoal()
    try:
        rclpy.spin(client_node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        # Destruir el cliente y el nodo antes de apagar
        client_node.destroy_node()
        rclpy.try_shutdown()

if __name__ == '__main__':
    main()