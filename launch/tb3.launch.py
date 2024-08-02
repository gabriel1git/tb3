import os
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    #caminho para o diretório do pacote
    package_dir = get_package_share_directory('tb3')

    #caminho para o arquivo d mundo
    world_file_name = 'tb3.world'
    world_files = os.path.join(package_dir, 'worlds',world_file_name)

    sdf_path = os.path.join(get_package_share_directory('tb3'),'models','tb3_model','model.sdf.xml')

    # Launch configuration variables specific to simulation
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    x_pose = LaunchConfiguration('x_pose', default='-7')
    y_pose = LaunchConfiguration('y_pose', default='-7')

    urdf = os.path.join(package_dir, 'tb3.urdf')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo','--verbose', world_files,'-s','libgazebo_ros_factory.so']),
        
            Node(
            name="Turtlebot3",
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=["-file",sdf_path, "-entity","tb3_model", "-x", x_pose, "-y", y_pose],
            output='screen',
        ),
        Node(
            package='tb3',
            executable='scan_map'
        ),

    ])