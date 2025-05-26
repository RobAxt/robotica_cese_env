# ROS2 Bag

## Robocup at Home 2024 Rosbags Dataset for storing groceries
[Dataset for storing groceries](https://zenodo.org/records/13749419)
```bash
~/robotica_cese_env/src/axt_pkg$ mkdir r2b_groceries
~/robotica_cese_env/src/axt_pkg$ cd r2b_groceries
~/robotica_cese_env/src/axt_pkg/r2b_groceries$ wget https://zenodo.org/records/13749419/files/storing%20groceries.zip
~/robotica_cese_env/src/axt_pkg/r2b_groceries$ unzip 'storing groceries.zip'
```
## Rosbag Content
```bash
~/ros2_ws/src/axt_pkg# ros2 bag info r2b_groceries/storing_try_2/

Files:             rosbag2_2024_07_18-17_27_55_0.db3
Bag size:          3.6 GiB
Storage id:        sqlite3
ROS Distro:        unknown
Duration:          84.449685350s
Start:             Jul 18 2024 15:27:56.073749955 (1721316476.073749955)
End:               Jul 18 2024 15:29:20.523435305 (1721316560.523435305)
Messages:          27004
Topic information: Topic: /bb_img_best_detection | Type: sensor_msgs/msg/Image | Count: 0 | Serialization Format: cdr
                   Topic: /cmd_vel | Type: geometry_msgs/msg/Twist | Count: 595 | Serialization Format: cdr
                   Topic: /head_front_camera/depth/image_raw | Type: sensor_msgs/msg/Image | Count: 2526 | Serialization Format: cdr
                   Topic: /head_front_camera/rgb/camera_info | Type: sensor_msgs/msg/CameraInfo | Count: 2530 | Serialization Format: cdr
                   Topic: /head_front_camera/rgb/image_raw | Type: sensor_msgs/msg/Image | Count: 2530 | Serialization Format: cdr
                   Topic: /joint_states | Type: sensor_msgs/msg/JointState | Count: 8446 | Serialization Format: cdr
                   Topic: /map | Type: nav_msgs/msg/OccupancyGrid | Count: 1 | Serialization Format: cdr
                   Topic: /robot_description | Type: std_msgs/msg/String | Count: 1 | Serialization Format: cdr
                   Topic: /say_text | Type: std_msgs/msg/String | Count: 1 | Serialization Format: cdr
                   Topic: /scan | Type: sensor_msgs/msg/LaserScan | Count: 1267 | Serialization Format: cdr
                   Topic: /scan_raw | Type: sensor_msgs/msg/LaserScan | Count: 1267 | Serialization Format: cdr
                   Topic: /tf | Type: tf2_msgs/msg/TFMessage | Count: 7833 | Serialization Format: cdr
                   Topic: /tf_static | Type: tf2_msgs/msg/TFMessage | Count: 7 | Serialization Format: cdr
Service:           0
Service information: 
```
## Ejecución Manual
```bash
~/ros2_ws# ros2 bag play src/axt_pkg/r2b_groceries/storing_try_2 -r2.0 --loop 
~/ros2_ws# ros2 run rqt_gui rqt_gui --perspective-file src/axt_pkg/config/rosbag.perspective 
~/ros2_ws# ros2 run rviz2 rviz2 -d src/axt_pkg/config/rosbag.rviz 
```
