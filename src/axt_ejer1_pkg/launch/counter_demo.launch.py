import launch
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    # Declare launch arguments
    counter_max_arg = launch.actions.DeclareLaunchArgument(
        'counter_max',
        default_value='60',
        description='Maximum count value before publisher shuts down'
    )

    timer_period_arg = launch.actions.DeclareLaunchArgument(
        'timer_period',
        default_value='0.2',
        description='Timer period in seconds for publishing counter values'
    )

    reset_counter_arg = launch.actions.DeclareLaunchArgument(
        'reset_counter',
        default_value='50',
        description='Count value at which reset counter'
    )


    # Create publisher node with counter_max parameter
    publisher_node = Node(
        package='axt_ejer1_pkg',
        executable='counter_publisher',
        name='counter_publisher',
        output='screen',
        parameters=[
            {'counter_max':LaunchConfiguration('counter_max')},
            {'timer_period':LaunchConfiguration('timer_period')}
        ],
        on_exit=launch.actions.Shutdown()
    )

    # Create subscriber node
    subscriber_node = Node(
        package='axt_ejer1_pkg',
        executable='counter_subscriber',
        name='counter_subscriber',
        output='screen',
        parameters=[
            {'reset_counter':LaunchConfiguration('reset_counter')}
        ],
    )

    # Create launch description and add nodes and arguments
    ld = launch.LaunchDescription()
    ld.add_action(counter_max_arg)
    ld.add_action(timer_period_arg)
    ld.add_action(reset_counter_arg)
    ld.add_action(publisher_node)
    ld.add_action(subscriber_node)
    
    return ld
