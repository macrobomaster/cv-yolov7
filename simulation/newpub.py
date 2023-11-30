import rclpy
from rclpy.node import Node
import diagnostic_msgs.msg
import std_msgs.msg
import random
import datetime
from geometry_msgs.msg import Twist


class DummyPublisherNode(Node):
    def __init__(self):
        super().__init__("dummypublisher")
        self.current_position = 0.0
        self.qii_diagnostics_publisher = self.create_publisher(
            Twist,
            "/red_standard_robot1/cmd_vel",
            10,
        )

        self.timer = self.create_timer(0.5, self.publish_random_values)

    def publish_random_values(self):
        twist_msg = Twist()
        twist_msg.linear.x = random.uniform(0, 1)
        twist_msg.linear.y = random.uniform(0, 1)
        twist_msg.linear.z = random.uniform(0, 1)
        twist_msg.angular.x = random.uniform(0, 1)
        twist_msg.angular.y = random.uniform(0, 1)
        twist_msg.angular.z = random.uniform(0, 1)        
        self.qii_diagnostics_publisher.publish(twist_msg)


def main(args=None):
    rclpy.init()
    node = DummyPublisherNode()
    print("Starting to publish random data")

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        print("interuppted ")
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()