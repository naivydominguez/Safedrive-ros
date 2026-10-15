import rclpy
from rclpy.node import Node
from std_msgs.msg import String


#creates a ROS2 node
class SafetyPublisher(Node):

    def __init__(self):
        super().__init__('safety_publisher')

        #creates a publisher that sends String messages through /safety_status
        self.publisher = self.create_publisher(
            String,
            '/safety_status',
            10 #specifies the depth of the message queue
        )

        #calls publish_status() ~once every second while the node is running
        self.timer = self.create_timer(
            1.0,
            self.publish_status
        )

    def publish_status(self):
        msg = String()
        msg.data = 'SAFE'

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Published: {msg.data}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = SafetyPublisher()

    rclpy.spin(node) #keeps node running & allows ROS2 to execute callbacks eg timer function

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
