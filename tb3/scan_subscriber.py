import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class Subscriber_lidar(Node):

    def __init__(self):
        super().__init__('subscriber_lidar')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.subscription = self.create_subscription(LaserScan, '/scan', self.listener_callback, 10)
        self.count = 0
        self.velocity = Twist()
        self.subscription  # prevent unused variable warning
        self.publisher  # prevent unused variable warning
        self.position_a = [0,-2]
        self.position_b = [0, 2]
    def listener_callback(self, msg):
        self.area = msg.ranges
    def timer_callback(self):
        self.velocity = Twist()
        self.velocity.linear.x = 0.0
        self.velocity.angular.z = 0.0 
        self.publisher.publish(self.velocity)
        self.get_logger().info('Publishing: "%s"' % self.velocity.linear.x)
    def go_to(self):
        s


def main(args=None):
    rclpy.init(args=args)

    subscriber_lidar = Subscriber_lidar()

    rclpy.spin(subscriber_lidar)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscriber_lidar.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()