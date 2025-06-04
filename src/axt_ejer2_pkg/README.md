# Ejericio 2

## Consigna
Crear un nodo que recibe un texto como action server y envía cada palabra del texto como feedback a 1Hz.

Crear otro nodo como action client que reciba un texto como argumento y lo envíe al primer nodo como action. Se subscribe al feedback del primero y lo muestra en la terminal. Cuando el primer nodo indica que terminó, el segundo nodo publica el mensaje “Texto republicado!”

Cree el mensaje custom para hacerlo.

Crear un roslaunch que permita pasar el texto como argumento y ejecute ambos nodos.

# Nodo Servidor
## Creacion de paquete
```bash
~/ros2_ws/src# ros2 pkg create axt_ejer2_pkg --build-type ament_python --dependencies rclpy axt_ejer2_interfaces 
```

## Compilacion de paquete
```bash
~/ros2_ws# colcon build --packages-select axt_ejer2_pkg
~/ros2_ws# source install/setup.bash
~/ros2_ws# 
```

## Ejecucion manual del server action
```bash
~/ros2_ws# ros2 run axt_ejer2_pkg splitWords_actionServer
```

## Verificacion de action server disponibles
```bash
~/ros2_ws# ros2 action list
/splitwords
```

## Pruebas manuales del servidor
```bash
~/ros2_ws# ros2 action send_goal /splitwords axt_ejer2_interfaces/action/SplitWords "{text: \"Hola mundo desde ROS 2\"}" --feedback
Waiting for an action server to become available...
Sending goal:
     text: Hola mundo desde ROS 2

Goal accepted with ID: 2a7c1ea1cd034290acfda1318b79540c

Feedback:
    current_word: Hola

Feedback:
    current_word: mundo

Feedback:
    current_word: desde

Feedback:
    current_word: ROS

Feedback:
    current_word: '2'

Result:
    total_words: 5

Goal finished with status: SUCCEEDED
```

# Nodo Cliente
## Ejecucion manual del cliente
```bash
~/ros2_ws# ros2 run axt_ejer2_pkg splitWords_actionClient --ros-args -p text:="Hola mundo desde ROS 2"
```

## Ejecucion automática
```bash
~/ros2_ws# ros2 launch axt_ejer2_pkg splitWordsAction_demo.launch.py text:="Hola mundo desde ROS 2"
```