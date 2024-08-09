import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    package_dir = os.path.join(get_package_share_directory('tb3'))
    #caminho para o arquivo config
    map_file = os.path.join(package_dir, "config", 'tb3_world_1.yaml')
    params_file = os.path.join(package_dir, "config", 'tb3_nav_params.yaml')
    rviz_config = os.path.join(package_dir, "config", 'tb3_nav.rviz')

    return LaunchDescription([

        # Integerating Nav2 Stack
        IncludeLaunchDescription(PythonLaunchDescriptionSource([
            get_package_share_directory('nav2_bringup'),'/launch','/bringup_launch.py']),
            launch_arguments={
                'map' :map_file,
                'params_file':params_file}.items(),
            ),
        Node(
            package='tb3',
            executable='way_points_2',
            name='way_points_map_2',
        ),

        # Rviz2 bringup
        Node(
            package='rviz2',
            output='screen',
            executable='rviz2',
            name='rviz2_node',
            arguments=['-d',rviz_config],
        ),
    ])