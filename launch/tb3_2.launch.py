import os
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
from math import pi

def generate_launch_description():
    #caminho para o diretório do pacote
    package_dir = get_package_share_directory('tb3')

    #caminho para o arquivo d mundo
    world_file_name = 'tb3_2.world'
    world_files = os.path.join(package_dir, 'worlds',world_file_name)

    sdf_path = os.path.join(get_package_share_directory('tb3'),'models','tb3_model2','model.sdf')

    # Launch configuration variables specific to simulation
    x_pose = LaunchConfiguration('x_pose', default='0.0')
    y_pose = LaunchConfiguration('y_pose', default='0.0')
    yaw_pose = LaunchConfiguration('y_pose', default= pi/2)

    urdf = os.path.join(package_dir, 'urdf', 'tb3.urdf')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo','--verbose', world_files,'-s','libgazebo_ros_factory.so']),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            arguments=[urdf]),

        Node(
            name="Turtlebot3",
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=["-file",sdf_path, "-entity","tb3_model2", "-x", x_pose, "-y", y_pose, "-Y", yaw_pose],
            output='screen',
        ),

    ])