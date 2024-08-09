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

    alvo_1 = [1.5, -1.5]
    alvo_2 = [0., -1.]
    alvo_3 = [-2., -1.97]
    alvo_4 = [-0.5, 1.97]
    alvo_5 = [-2.3, 1.97]
    alvo_6 = [-2.3, -1.]
    alvo_7 = [-1.5, 0.]
    alvo_8 = [-2., 1.]
    alvo_9 = [1.5, 1.5]
    alvo_10 = [0., 0.]

    # -- init
    rclpy.init()
    nav = BasicNavigator()

    # -- Set initial pose
    initial_pose = create_pose_stamped(nav, 0.0, 0.0, 0.0)
    nav.setInitialPose(initial_pose)

    # -- Wait for nav2
    nav.waitUntilNav2Active()

    # -- Send Nav2 goal
    goal_pose1 = create_pose_stamped(nav, alvo_1[0], alvo_1[1], -pi/2)
    goal_pose2 = create_pose_stamped(nav, alvo_2[0], alvo_2[1], pi)
    goal_pose3 = create_pose_stamped(nav, alvo_3[0], alvo_3[1], 0.0)
    goal_pose4 = create_pose_stamped(nav, alvo_4[0], alvo_4[1], pi)
    goal_pose5 = create_pose_stamped(nav, alvo_5[0], alvo_5[1], -pi/2)
    goal_pose6 = create_pose_stamped(nav, alvo_6[0], alvo_6[1], 0.0)
    goal_pose7 = create_pose_stamped(nav, alvo_7[0], alvo_7[1], pi/2)
    goal_pose8 = create_pose_stamped(nav, alvo_8[0], alvo_8[1], 0.0)
    goal_pose9 = create_pose_stamped(nav, alvo_9[0], alvo_9[1], pi/2)
    goal_pose10 = create_pose_stamped(nav, alvo_10[0], alvo_10[1], 0.0)

    # -- Follow waypoints
    waypoints = [goal_pose1, goal_pose2, goal_pose3, goal_pose4, goal_pose5, goal_pose6, goal_pose7, goal_pose8, goal_pose9, goal_pose10]
    nav.followWaypoints(waypoints)
    while not nav.isTaskComplete():
        feedback = nav.getFeedback()
        print(feedback)

    print(nav.getResult())

    # -- shuntdown
    rclpy.shutdown()

if __name__ == '__main__':
    main()