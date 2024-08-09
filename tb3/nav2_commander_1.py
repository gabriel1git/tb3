#!/usr/bin/env python3
import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped, Quaternion
from math import sin, cos, pi

def create_pose_stamped(navigator: BasicNavigator, position_x, position_y, orientation_z):
    q = euler_to_quaternion(0.0, 0.0, orientation_z)
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = navigator.get_clock().now().to_msg()
    # -- Position
    pose.pose.position.x = position_x
    pose.pose.position.y = position_y
    pose.pose.position.z = 0.0
    # -- Orientation
    pose.pose.orientation.x = q.x
    pose.pose.orientation.y = q.y
    pose.pose.orientation.z = q.z
    pose.pose.orientation.w = q.w
    return pose

def euler_to_quaternion(roll, pitch, yaw):
    qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - cos(roll/2) * sin(pitch/2) * sin(yaw/2)
    qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + sin(roll/2) * cos(pitch/2) * sin(yaw/2)
    qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - sin(roll/2) * sin(pitch/2) * cos(yaw/2)
    qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2) + sin(roll/2) * sin(pitch/2) * sin(yaw/2)
    return Quaternion(x=qx, y=qy, z=qz, w=qw)

def main():

    alvo_1 = [5., 4.]
    alvo_2 = [4., -4.]

    # -- init
    rclpy.init()
    nav = BasicNavigator()

    # -- Set initial pose
    initial_pose = create_pose_stamped(nav, -5.0, -6.0, 0.0)
    nav.setInitialPose(initial_pose)

    # -- Wait for nav2
    nav.waitUntilNav2Active()

    # -- Send Nav2 goal
    goal_pose1 = create_pose_stamped(nav, alvo_1[0] + 2., alvo_1[1] + 1., pi/2.)
    goal_pose2 = create_pose_stamped(nav, alvo_2[0] + 2., alvo_2[1] + 1., -pi-2)

    # -- Follow waypoints
    waypoints = [goal_pose1, goal_pose2]
    nav.followWaypoints(waypoints)
    while not nav.isTaskComplete():
        feedback = nav.getFeedback()
        print(feedback)

    print(nav.getResult())

    # -- shuntdown
    rclpy.shutdown()

if __name__ == '__main__':
    main()