import launch
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    # Declare launch arguments
    text_arg = launch.actions.DeclareLaunchArgument(
        'text',
        default_value='The quick brown fox jumps over the lazy dog.',
        description='String to be splitter'
    )

    # Create action server node
    actionServer_node = Node(
        package='axt_ejer2_pkg',
        executable='splitWords_actionServer',
        name='splitWords_actionServer',
        output='screen',
        parameters=[ ],
    )

    # Create action client node
    actionClient_node = Node(
        package='axt_ejer2_pkg',
        executable='splitWords_actionClient',
        name='splitWords_actionClient',
        output='screen',
        parameters=[
            {'text':LaunchConfiguration('text')}
        ],
    )

    # Create launch description and add nodes and arguments
    ld = launch.LaunchDescription()
    ld.add_action(text_arg)
    ld.add_action(actionServer_node)
    ld.add_action(actionClient_node)
    
    return ld