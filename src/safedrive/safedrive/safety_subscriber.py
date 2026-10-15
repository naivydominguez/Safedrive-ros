import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SafetySubscriber(Node):

    def __init__(self):
        super().__init__('safety_subscriber')

        self.subscription = self.create_subscription(
            String,
            '/safety_status',
            self.status_callback,
            10
        )

    #Ros calls this func whenever a new message arrives
    def status_callback(self, msg):
        self.get_logger().info(
            f'Received safety status: {msg.data}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = SafetySubscriber()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
