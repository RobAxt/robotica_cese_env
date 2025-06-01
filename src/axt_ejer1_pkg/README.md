# Ejericio 1

## Consigna
Proveer un paquete de ROS con un launchfile con dos nodos:

* Un nodo publica cinco veces por segundo un contador. Este nodo tiene un servicio que resetea su contador.
* Un segundo nodo está suscrito al primero y cuando el mensaje con el contador llega a 50 (cada 10 segundos), resetea el contador del nodo.
* Ambos nodos pueden configurar por parámetros:
    * Nodo publicando:
        * Frecuencia que publica.
        * Cantidad máxima que publica.
    * Nodo suscrito:
        * A qué número reinicia el contador del nodo.
* Launchfile que lance todo y permita

## Creacion de paquete
```bash
~/ros2_ws/src# ros2 pkg create --build-type ament_python axt_ejer1_pkg
```

## Compilacion de paquete
```bash
~/ros2_ws# colcon build --packages-select axt_ejer1_pkg
~/ros2_ws# source install/setup.bash
~/ros2_ws# 
```
# Nodo Publicador y Server Service
## Ejecucion manual 
```bash
# Default configuration (counts to 100, publishes every 0.2 second)
~/ros2_ws# ros2 run axt_ejer1_pkg counter_publisher

# Custom configuration (counts to 51, publishes every 2.0 seconds)
~/ros2_ws# ros2 run axt_ejer1_pkg counter_publisher --ros-args -p counter_max:=51 -p timer_period:=2.0
```

## Informacion del publicador (mientras esta corriendo)
```bash
~/ros2_ws# ros2 node list
/counter_publisher

~/ros2_ws# ros2 node info /counter_publisher
/counter_publisher
  Subscribers:

  Publishers:
    /counter_topic: std_msgs/msg/Int32
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
  Service Servers:
    /counter_publisher/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /counter_publisher/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /counter_publisher/get_parameters: rcl_interfaces/srv/GetParameters
    /counter_publisher/get_type_description: type_description_interfaces/srv/GetTypeDescription
    /counter_publisher/list_parameters: rcl_interfaces/srv/ListParameters
    /counter_publisher/set_parameters: rcl_interfaces/srv/SetParameters
    /counter_publisher/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
    /reset_counter: std_srvs/srv/Trigger
  Service Clients:

  Action Servers:

  Action Clients:

~/ros2_ws# ros2 service info /reset_counter 
Type: std_srvs/srv/Trigger
Clients count: 0
Services count: 1

~/ros2_ws# ros2 topic info /counter_topic 
Type: std_msgs/msg/Int32
Publisher count: 1
Subscription count: 0
```

## Invocar al servicio del counter_publisher desde linea de comando
```bash
~/ros2_ws# ros2 service call /reset_counter std_srvs/srv/Trigger "{}"
```

# Nodo Suscriptor y Client Service
## Ejecucion manual 
```bash
# Default configuration (resets at count 50)
~/ros2_ws# ros2 run axt_ejer1_pkg counter_subscriber

# Custom configuration (counts to 51, publishes every 2.0 seconds)
~/ros2_ws# ros2 run axt_ejer1_pkg counter_subscriber  --ros-args -p reset_counter:=3
```
## Informacion del publicador y suscriptor (mientras estána corriendo)
```bash
~/ros2_ws# ros2 node list
/counter_publisher
/counter_subscriber
~/ros2_ws# ros2 node info /counter_subscriber
/counter_subscriber
  Subscribers:
    /counter_topic: std_msgs/msg/Int32
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
  Service Servers:
    /counter_subscriber/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /counter_subscriber/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /counter_subscriber/get_parameters: rcl_interfaces/srv/GetParameters
    /counter_subscriber/get_type_description: type_description_interfaces/srv/GetTypeDescription
    /counter_subscriber/list_parameters: rcl_interfaces/srv/ListParameters
    /counter_subscriber/set_parameters: rcl_interfaces/srv/SetParameters
    /counter_subscriber/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:
    /reset_counter: std_srvs/srv/Trigger
  Action Servers:

  Action Clients:

~/ros2_ws# ros2 service info /reset_counter 
Type: std_srvs/srv/Trigger
Clients count: 1
Services count: 1

~/ros2_ws# ros2 topic info /counter_topic 
Type: std_msgs/msg/Int32
Publisher count: 1
Subscription count: 1

```