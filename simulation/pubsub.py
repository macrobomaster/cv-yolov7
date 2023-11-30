import rclpy
from geometry_msgs.msg import Twist
import random
import time

def publish_random_twists():
    rclpy.init()

    # Create a ROS 2 node
    node = rclpy.create_node('random_twist_publisher')

    # Create a publisher for the Twist message
    publisher = node.create_publisher(Twist, '/red_standard_robot1/cmd_vel', 10)

    # Define the rate (10 Hz)
    rate = node.create_rate(10)

    # Loop to publish random Twist messages
    while rclpy.ok():
        
        twist_msg = Twist()
        twist_msg.linear.x = random.uniform(0, 1)
        twist_msg.linear.y = random.uniform(0, 1)
        twist_msg.linear.z = random.uniform(0, 1)
        twist_msg.angular.x = random.uniform(0, 1)
        twist_msg.angular.y = random.uniform(0, 1)
        twist_msg.angular.z = random.uniform(0, 1)

        # Publish the Twist message
        publisher.publish(twist_msg)

        # Log the published values
        node.get_logger().info(f"Published Twist: {twist_msg}")

        # Sleep to achieve the desired rate
        rate.sleep()

    # Cleanup
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    publish_random_twists()
