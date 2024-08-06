import rclpy
from rclpy.node import Node
import numpy as np
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist


class Subscriber_lidar(Node):

    def __init__(self):
        super().__init__('subscriber_lidar')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.sub_odom = self.create_subscription(Odometry, '/odom', self.listener_odom, 10)
        self.sub_scan = self.create_subscription(LaserScan, '/scan', self.listener_scan, 10)
        self.count = 0
        self.velocity = Twist()
        self.sub_odom  # prevent unused variable warning
        self.sub_scan
        self.publisher  # prevent unused variable warning
        self.position_a = np.array([0,7])
        self.position_b = np.array([4, -4])
        self.current_position = np.array([0., 0.]) #[x, y]
        self.current_orientation = np.array([0., 0., 0., 0.]) #[x, y, z, w]
        self.velocity_angular = 0.
        self.velocity_linear = 0.
        self.yaw = 0.
        self.align = False
        self.desvio_esquerda = False
        self.desvio_direita = False

    def listener_odom(self, msg):

        self.current_position[0] = round(msg.pose.pose.position.x,4)
        self.current_position[1] = round(msg.pose.pose.position.y,4)

        self.current_orientation[0] = round(msg.pose.pose.orientation.x,4)
        self.current_orientation[1] = round(msg.pose.pose.orientation.y,4)
        self.current_orientation[2] = round(msg.pose.pose.orientation.z,4)
        self.current_orientation[3] = round(msg.pose.pose.orientation.w,4)
        self.yaw = np.arctan2(2*(self.current_orientation[3] * self.current_orientation[2] + self.current_orientation[0] * self.current_orientation[1]), 1 - 2 * ((self.current_orientation[1]**2) + (self.current_orientation[2]**2)))
        #self.get_logger().info('yaw: "%s"' % (self.yaw))
        self.go_to()

    def listener_scan(self,msg):
        self.range = msg.ranges
        #self.get_logger().info('angle: "%s"' % (self.range))

    def timer_callback(self):
        self.velocity = Twist()
        self.velocity.linear.x = self.velocity_linear
        self.velocity.angular.z = self.velocity_angular 
        self.publisher.publish(self.velocity)

    def go_to(self):
        angle_goal = np.arctan2(self.position_a[0] - self.current_position[0], self.position_a[1] - self.current_position[1])
        distance = np.linalg.norm(self.position_a - self.current_position)

        #align with goal position
        '''if (self.yaw > 0) and (self.yaw < angle_goal):
            if ((angle_goal - self.yaw) > 0.001) and self.align == False:
                self.velocity_angular = 0.1
                self.velocity_linear = 0.
                self.get_logger().info('Aligning + ...')
        elif(self.yaw > 0) and (self.yaw > angle_goal):
            if ((self.yaw - angle_goal) > 0.001) and self.align == False:
                self.velocity_angular = -0.1
                self.velocity_linear = 0.
                self.get_logger().info('Aligning - ...')
        elif(self.yaw < 0) and (self.yaw < angle_goal):
            if ((self.yaw - angle_goal) > 0.001) and self.align == False:
                self.velocity_angular = -0.1
                self.velocity_linear = 0.
                self.get_logger().info('Aligning - ...')
        elif(self.yaw > 0) and (self.yaw > angle_goal):
            if ((self.yaw - angle_goal) > 0.001) and self.align == False:
                self.velocity_angular = -0.1
                self.velocity_linear = 0.
                self.get_logger().info('Aligning - ...')
            elif(angle_goal - self.yaw) < 0.0011 and self.align == False:
                self.align = True
                self.velocity_angular = 0.0
                self.velocity_linear = 0.4
                self.get_logger().info('Aligned ...')
                self.get_logger().info('To goal ...')
        elif self.yaw < 0:
            if ((angle_goal + self.yaw) > 0.001) and self.align == False:
                self.velocity_angular = 0.1
                self.velocity_linear = 0.
                self.get_logger().info('Aligning ...')
            elif(angle_goal - self.yaw) < 0.0011 and self.align == False:
                self.align = True
                self.velocity_angular = 0.0
                self.velocity_linear = 0.4
                self.get_logger().info('Aligned ...')
                self.get_logger().info('To goal ...')
        
        #wall left
        if self.range[115] < 1.:
            self.get_logger().info('Parede a direita: %s' % self.range[115])
            self.velocity_linear = 0.
            self.velocity_angular = 0.1
            self.desvio_direita = True
        elif (self.range[115] > 1.)and (self.desvio_direita == True):
            self.get_logger().info('desviando ...')
            self.velocity_angular = 0.0
            self.velocity_linear = 0.2
            self.desvio_direita = False
            

        #wall right
        if self.range[155] < 1.:
            self.get_logger().info('Parede a esquerda ...')
            self.velocity_linear = 0.
            self.velocity_angular = -0.1
            self.desvio_esquerda = True
        if (self.range[155] > 1.)and (self.desvio_esquerda == True):
            self.get_logger().info('desviando ...')
            self.velocity_angular = 0.0
            self.velocity_linear = 0.2
            if self.range[220] > 1.5:
                self.align = False
                self.desvio_esquerda = False'''

        self.get_logger().info('angle: "%s"' % (self.yaw))


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