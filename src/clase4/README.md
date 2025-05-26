# Comandos usados en clase 04

# Sourcear la consola
```bash
# source install/setup.bash
```

# Creacion de un paquete
```bash
# ros2 pkg create --build-type ament_cmake prueba
```

# Compilacion de paquete
```bash
# cd prueba
# colcon build
# colcon build --packages-select axt_pkg
```

# Launch tortuguitas
```bash
# ros2 launch clase4 multisim.launch.py
```

# Launch tortuguitas + GUI
```bash
# ros2 launch clase4 node_analysis.launch.py gui:=true
```

# Para ver que hace un launch
```bash
# ros2 launch clase4 node_analysis.launch.py --print-description
```

# Para ver opciones que dispone un launch
```bash
#  ros2 launch clase4 node_analysis.launch.py --show-arguments
```

# Para ver los nodos que estan corriendo en ros2
```bash
# ros2 node list
```

# Para ver los nodos de ros2 que estan disponibles
```bash
# ros2 topic list
```

# Para rotar una de las tortugas
```bash
# ros2 topic pub /turtlesim1/turtle1/cmd_vel geometry_msgs/msg/Twist 'linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 1.0
' -r10.0
```

# Para ver que mensajes se estan pasande de un topico especifico
```bash
# ros2 topic echo /turtlesim1/turtle1/cmd_vel
```

# Para ver rqt gui
```bash
# ros2 run rqt_gui rqt_gui --perspective-file src/axt_pkg/config/rosbag.perspective
```

# Para ver RViz
```bash
# ros2 run rviz2 rviz2 -d src/axt_pkg/config/rosbag.rviz
```

# Para reproducir un rosbag
```bash
# ros2 bag play src/axt_pkg/r2b_groceries/storing_try_2 -r2.0 --loop
```

# Para plotear el valor de velocidad
```bash
# ros2 run rqt_plot rqt_plot
```

