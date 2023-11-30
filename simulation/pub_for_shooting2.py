import rclpy
from rclpy.node import Node
import diagnostic_msgs.msg
import std_msgs.msg
import random
import datetime
from rmoss_interfaces.msg import ShootCmd



class DummyPublisherNode(Node):
    def __init__(self):
        super().__init__("dummyshooter")
        self.current_position = 0.0
        self.qii_diagnostics_publisher = self.create_publisher(
            ShootCmd,
            "/blue_standard_robot1/robot_base/shoot_cmd",
            10,
        )

        self.timer = self.create_timer(0.5, self.getShootCmdMsg)

    # def publish_random_values(self):
    #     twist_msg = Twist()
    #     twist_msg.linear.x = random.uniform(0, 1)
    #     twist_msg.linear.y = random.uniform(0, 1)
    #     twist_msg.linear.z = random.uniform(0, 1)
    #     twist_msg.angular.x = random.uniform(0, 1)
    #     twist_msg.angular.y = random.uniform(0, 1)
    #     twist_msg.angular.z = random.uniform(0, 1)        
    #     self.qii_diagnostics_publisher.publish(twist_msg)
    def getShootCmdMsg(self, ):
        msg = ShootCmd()
        msg.projectile_num=random.randint(0, 100)
        msg.projectile_velocity=random.uniform(0, 2)
        self.qii_diagnostics_publisher.publish(msg) 


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