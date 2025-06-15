## axtbot
```bash
$ docker exec -it robotica_cese_env-dev-1 bash

~/ros2_ws# source install/setup.bash

~/ros2_ws# colcon build --packages-select mycobot_description

~/ros2_ws# colcon build --packages-select mycobot_gazebo

~/ros2_ws# ros2 launch mycobot_gazebo mycobot.gazebo.launch.py     load_controllers:=true     world_file:=pick_and_place_demo.world     use_camera:=true     use_rviz:=false     use_robot_state_pub:=true     use_sim_time:=true     robot_model:=axtbot     x:=0.0     y:=0.0     z:=1.05     roll:=0.0     pitch:=0.0     yaw:=0.0 &

```