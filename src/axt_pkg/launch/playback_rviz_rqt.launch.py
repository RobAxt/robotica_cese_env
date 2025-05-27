import os
import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.actions import LogInfo
from launch.conditions import IfCondition
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import TextSubstitution
from launch.actions import ExecuteProcess

def generate_launch_description():

    # Definicion de Path
    bag_path = os.path.join(os.path.join('/root', 'ros2_ws', 'src', 'axt_pkg', 'r2b_groceries', 'storing_try_2'))
    rviz_config = os.path.join(get_package_share_directory('axt_pkg'), 'config', 'rosbag.rviz')
    rqt_persp = os.path.join(get_package_share_directory('axt_pkg'), 'config', 'rosbag.perspective')

    # Mensajes de usuario de inicializacion
    bag_message  = LogInfo(msg=['Reproduciendo rosbag: ', bag_path])
    rviz_message = LogInfo(msg=['Abriendo RVIZ con la configuracion: ', rviz_config])
    rqt_message  = LogInfo(msg=['Abriendo RQT con la perspectiva: ', rqt_persp])

    # Definicion de nodos
    rqt_node = Node(package='rqt_gui', executable='rqt_gui', name='rqt_groceries',
        arguments=['--perspective-file', TextSubstitution(text=rqt_persp)])

    rviz_node = Node(package='rviz2', executable='rviz2', name='rviz_groceries',
        arguments=['-d', TextSubstitution(text=rviz_config)])

    # https://github.com/ros2/rosbag2?tab=readme-ov-file#using-in-launch
    bag_node = launch.actions.ExecuteProcess(
        cmd=['ros2','bag','play', bag_path, '-r2.0', '--loop']) 
    
    # Create the launch description and populate
    ld = LaunchDescription()

    # Add any actions
    ld.add_action(bag_message)
    ld.add_action(bag_node)    
    ld.add_action(rqt_message)
    ld.add_action(rqt_node)
    ld.add_action(rviz_message)
    ld.add_action(rviz_node)

    return ld