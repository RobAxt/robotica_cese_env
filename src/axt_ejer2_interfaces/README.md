# Ejericio 2

## Consigna
Crear un nodo que recibe un texto como action server y envía cada palabra del texto como feedback a 1Hz.

Crear otro nodo como action client que reciba un texto como argumento y lo envíe al primer nodo como action. Se subscribe al feedback del primero y lo muestra en la terminal. Cuando el primer nodo indica que terminó, el segundo nodo publica el mensaje “Texto republicado!”

Cree el mensaje custom para hacerlo.

Crear un roslaunch que permita pasar el texto como argumento y ejecute ambos nodos.

## Creacion de la interface
```bash
~/ros2_ws/src# ros2 pkg create axt_ejer2_interfaces
```

## Compilacion de paquete
```bash
~/ros2_ws# colcon build --packages-select axt_ejer2_interfaces
~/ros2_ws# source install/setup.bash

```

## Verificar si aparece la interface custom action
```bash
~/ros2_ws# ros2 interface show axt_ejer2_pkg/action/SplitWords
```







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