import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException

from std_msgs.msg import Int32    # https://docs.ros.org/en/noetic/api/std_msgs/html/msg/Int32.html
from std_srvs.srv import Trigger  # https://docs.ros.org/en/noetic/api/std_srvs/html/srv/Trigger.html


class CounterSubscriber(Node):
    def __init__(self):
        super().__init__('counter_subscriber')

        # Se declara argumento de entrada
        self.declare_parameter('reset_counter', 50)
        self.reset_counter = self.get_parameter('reset_counter').get_parameter_value().integer_value
        self.get_logger().info(f'Counter will be reset at ({self.reset_counter})')


        # Se crea el servicio cliente para acceder
        self.reset_client = self.create_client(Trigger, '/reset_counter')

        # Se espera a que el servicio este creado por un servidor
        if not self.reset_client.wait_for_service(timeout_sec=5.0):
            self.get_logger().error(
                'El servicio /reset_counter NO respondió después de 5 segundos. '
                'Verifica que el servidor esté levantado y que el nombre sea correcto.'
            )

        # Se crea el request para Trigger es un request vacío
        self.request = Trigger.Request()

        self.subscription = self.create_subscription(
            Int32,
            'counter_topic',
            self.subscription_listener_callback,
            10)

    def subscription_listener_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')
        if  msg.data >= self.reset_counter:
            self.get_logger().info(f'Counter reached ({self.reset_counter}), calling service /reset_counter')
            self.future = self.reset_client.call_async(self.request)
            self.future.add_done_callback(self.service_response_callback) #  https://youtu.be/vCTbUgw6k8U?si=hGqjJO6da2HTqQHj&t=620
    
    def service_response_callback(self, future):
        if self.future.done() and not self.future.cancelled():
            response = self.future.result()  # Trigger.Response
            if response is not None:
                self.get_logger().info(f'Respuesta recibida: success={response.success} message="{response.message}"')
            else:
                self.get_logger().error('Se obtuvo respuesta nula del servicio.')
        else:
            self.get_logger().error('La llamada al servicio falló o fue cancelada.')


def main(args=None):
    rclpy.init(args=args)
    node = CounterSubscriber()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()

if __name__ == '__main__':
    main()
