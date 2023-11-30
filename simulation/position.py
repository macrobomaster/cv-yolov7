import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CmdVelSubscriber(Node):
    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            '/red_standard_robot1/cmd_vel',
            self.cmd_vel_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.get_logger().info('CmdVelSubscriber has started')

    def cmd_vel_callback(self, msg):
        linear = msg.linear
        angular = msg.angular
        self.get_logger().info(
            f'Received cmd_vel: Linear(x={linear.x}, y={linear.y}, z={linear.z}), '
            f'Angular(x={angular.x}, y={angular.y}, z={angular.z})')

def main(args=None):
    rclpy.init(args=args)
    subscriber = CmdVelSubscriber()
    try:
        rclpy.spin(subscriber)
    except KeyboardInterrupt:
        pass

    subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
