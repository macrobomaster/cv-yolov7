


import rclpy
from rclpy.node import Node
import diagnostic_msgs.msg
import std_msgs.msg
import random
import datetime
from geometry_msgs.msg import Twist


class State(Node):
    def __init__(self):
        super().__init__("state_control")
        self.last_ref_message = None
        self.last_camera_message = None
        self.last_lidar_message = None
        self.current_position = 0.0
        self.qii_diagnostics_publisher = self.create_publisher(
            Twist,
            "/red_standard_robot1/cmd_vel",
            10,
        )
        self.referee_subscriber = self.create_subscription(
            std_msgs.msg.String,
            "/referee_system/blue_standard_robot1/robot_status",
            self.referee_callback,
            10,
        )
        self.camera_subscriber = self.create_subscription(
            std_msgs.msg.String,
            "/red_standard_robot1/front_camera/image",
            self.camera_callback,
            10,
        )
    
    def referee_callback(self, msg):
        self.last_ref_message = msg
        print("Received referee message: ", self.last_ref_message)

    def publish_command(self, linear, angular):
        twist_msg = Twist()
        twist_msg.linear.x = linear[0]
        twist_msg.linear.y = linear[1]
        twist_msg.linear.z = linear[2] 
        twist_msg.angular.x = angular[0]
        twist_msg.angular.y = angular[1]
        twist_msg.angular.z = angular[2] 
        self.qii_diagnostics_publisher.publish(twist_msg)




def main(args=None):
    rclpy.init()
    node = State()
    print("Starting to publish random data")

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        print("interuppted ")
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()