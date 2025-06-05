# Ejercicio 2

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
[INFO] [1748999729.039861932] [split_words_action_client]: [Cliente] Enviando goal con texto: "Hola mundo desde ROS 2"
[INFO] [1748999729.041465932] [split_words_action_client]: [Cliente] Goal aceptado. Esperando resultado...
[INFO] [1748999729.041857785] [split_words_action_client]: [Cliente][Feedback] Palabra actual: "Hola"
[INFO] [1748999730.042440257] [split_words_action_client]: [Cliente][Feedback] Palabra actual: "mundo"
[INFO] [1748999731.043240367] [split_words_action_client]: [Cliente][Feedback] Palabra actual: "desde"
[INFO] [1748999732.044111918] [split_words_action_client]: [Cliente][Feedback] Palabra actual: "ROS"
[INFO] [1748999733.044715380] [split_words_action_client]: [Cliente][Feedback] Palabra actual: "2"
[INFO] [1748999734.046039164] [split_words_action_client]: [Cliente] Acción completada con éxito. Total de palabras: 5

~/ros2_ws# ros2 run axt_ejer2_pkg splitWords_actionClient 
[INFO] [1748999676.245768192] [split_words_action_client]: [Cliente] Enviando goal con texto: "Sphinx of black quartz, judge my vow."
[INFO] [1748999683.129921534] [split_words_action_client]: [Cliente] Goal aceptado. Esperando resultado...
[INFO] [1748999683.130402492] [split_words_action_client]: [Cliente][Feedback] Palabra actual: "Sphinx"
[INFO] [1748999684.130999828] [split_words_action_client]: [Cliente][Feedback] Palabra actual: "of"
[INFO] [1748999685.131728404] [split_words_action_client]: [Cliente][Feedback] Palabra actual: "black"
[INFO] [1748999686.132523421] [split_words_action_client]: [Cliente][Feedback] Palabra actual: "quartz,"
[INFO] [1748999687.133193928] [split_words_action_client]: [Cliente][Feedback] Palabra actual: "judge"
[INFO] [1748999688.133925456] [split_words_action_client]: [Cliente][Feedback] Palabra actual: "my"
[INFO] [1748999689.134664126] [split_words_action_client]: [Cliente][Feedback] Palabra actual: "vow."
[INFO] [1748999690.136223977] [split_words_action_client]: [Cliente] Acción completada con éxito. Total de palabras: 7
```

## Ejecucion automática
```bash
~/ros2_ws# ros2 launch axt_ejer2_pkg splitWordsAction_demo.launch.py text:="Hola mundo desde ROS 2"
[INFO] [launch]: All log files can be found below /root/.ros/log/2025-06-04-01-16-13-741337-itba-1211
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [splitWords_actionServer-1]: process started with pid [1214]
[INFO] [splitWords_actionClient-2]: process started with pid [1215]
[splitWords_actionServer-1] [INFO] [1748999773.916408578] [splitWords_actionServer]: [Inicio] SplitWords Action Server inicializado y a la espera de goals...
[splitWords_actionClient-2] [INFO] [1748999774.164076447] [splitWords_actionClient]: [Cliente] Enviando goal con texto: "Hola mundo desde ROS 2"
[splitWords_actionServer-1] [INFO] [1748999774.165109131] [splitWords_actionServer]: [GoalAceptado] Recibido texto con 5 palabras.
[splitWords_actionServer-1] [INFO] [1748999774.165673425] [splitWords_actionServer]: [Ejecutando] Iniciando procesamiento de SplitWords…
[splitWords_actionClient-2] [INFO] [1748999774.165927514] [splitWords_actionClient]: [Cliente] Goal aceptado. Esperando resultado...
[splitWords_actionServer-1] [INFO] [1748999774.165930848] [splitWords_actionServer]: [Feedback] "Hola" (1/5)
[splitWords_actionClient-2] [INFO] [1748999774.166339966] [splitWords_actionClient]: [Cliente][Feedback] Palabra actual: "Hola"
[splitWords_actionServer-1] [INFO] [1748999775.166596123] [splitWords_actionServer]: [Feedback] "mundo" (2/5)
[splitWords_actionClient-2] [INFO] [1748999775.167030882] [splitWords_actionClient]: [Cliente][Feedback] Palabra actual: "mundo"
[splitWords_actionServer-1] [INFO] [1748999776.167303083] [splitWords_actionServer]: [Feedback] "desde" (3/5)
[splitWords_actionClient-2] [INFO] [1748999776.167720063] [splitWords_actionClient]: [Cliente][Feedback] Palabra actual: "desde"
[splitWords_actionServer-1] [INFO] [1748999777.168056300] [splitWords_actionServer]: [Feedback] "ROS" (4/5)
[splitWords_actionClient-2] [INFO] [1748999777.168528132] [splitWords_actionClient]: [Cliente][Feedback] Palabra actual: "ROS"
[splitWords_actionServer-1] [INFO] [1748999778.168736649] [splitWords_actionServer]: [Feedback] "2" (5/5)
[splitWords_actionClient-2] [INFO] [1748999778.169190054] [splitWords_actionClient]: [Cliente][Feedback] Palabra actual: "2"
[splitWords_actionServer-1] [INFO] [1748999779.169404857] [splitWords_actionServer]: [Success] Acción completada. Total de palabras: 5
[splitWords_actionClient-2] [INFO] [1748999779.170513155] [splitWords_actionClient]: [Cliente] Acción completada con éxito. Total de palabras: 5
[INFO] [splitWords_actionClient-2]: process has finished cleanly [pid 1215]
^C[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[INFO] [splitWords_actionServer-1]: process has finished cleanly [pid 1214]

~/ros2_ws# ros2 launch axt_ejer2_pkg splitWordsAction_demo.launch.py
[INFO] [launch]: All log files can be found below /root/.ros/log/2025-06-04-01-17-00-606457-itba-1244
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [splitWords_actionServer-1]: process started with pid [1247]
[INFO] [splitWords_actionClient-2]: process started with pid [1248]
[splitWords_actionServer-1] [INFO] [1748999820.784095071] [splitWords_actionServer]: [Inicio] SplitWords Action Server inicializado y a la espera de goals...
[splitWords_actionClient-2] [INFO] [1748999820.787318469] [splitWords_actionClient]: [Cliente] Enviando goal con texto: "The quick brown fox jumps over the lazy dog."
[splitWords_actionServer-1] [INFO] [1748999820.788294959] [splitWords_actionServer]: [GoalAceptado] Recibido texto con 9 palabras.
[splitWords_actionServer-1] [INFO] [1748999820.788925035] [splitWords_actionServer]: [Ejecutando] Iniciando procesamiento de SplitWords…
[splitWords_actionServer-1] [INFO] [1748999820.789319907] [splitWords_actionServer]: [Feedback] "The" (1/9)
[splitWords_actionClient-2] [INFO] [1748999820.789396228] [splitWords_actionClient]: [Cliente] Goal aceptado. Esperando resultado...
[splitWords_actionClient-2] [INFO] [1748999820.790065139] [splitWords_actionClient]: [Cliente][Feedback] Palabra actual: "The"
[splitWords_actionServer-1] [INFO] [1748999821.790043112] [splitWords_actionServer]: [Feedback] "quick" (2/9)
[splitWords_actionClient-2] [INFO] [1748999821.790363352] [splitWords_actionClient]: [Cliente][Feedback] Palabra actual: "quick"
[splitWords_actionServer-1] [INFO] [1748999822.790746690] [splitWords_actionServer]: [Feedback] "brown" (3/9)
[splitWords_actionClient-2] [INFO] [1748999822.791090350] [splitWords_actionClient]: [Cliente][Feedback] Palabra actual: "brown"
[splitWords_actionServer-1] [INFO] [1748999823.791457347] [splitWords_actionServer]: [Feedback] "fox" (4/9)
[splitWords_actionClient-2] [INFO] [1748999823.791759424] [splitWords_actionClient]: [Cliente][Feedback] Palabra actual: "fox"
[splitWords_actionServer-1] [INFO] [1748999824.792191584] [splitWords_actionServer]: [Feedback] "jumps" (5/9)
[splitWords_actionClient-2] [INFO] [1748999824.792576640] [splitWords_actionClient]: [Cliente][Feedback] Palabra actual: "jumps"
[splitWords_actionServer-1] [INFO] [1748999825.792913180] [splitWords_actionServer]: [Feedback] "over" (6/9)
[splitWords_actionClient-2] [INFO] [1748999825.793273805] [splitWords_actionClient]: [Cliente][Feedback] Palabra actual: "over"
[splitWords_actionServer-1] [INFO] [1748999826.793630975] [splitWords_actionServer]: [Feedback] "the" (7/9)
[splitWords_actionClient-2] [INFO] [1748999826.793990923] [splitWords_actionClient]: [Cliente][Feedback] Palabra actual: "the"
[splitWords_actionServer-1] [INFO] [1748999827.794423519] [splitWords_actionServer]: [Feedback] "lazy" (8/9)
[splitWords_actionClient-2] [INFO] [1748999827.795111816] [splitWords_actionClient]: [Cliente][Feedback] Palabra actual: "lazy"
[splitWords_actionServer-1] [INFO] [1748999828.795140303] [splitWords_actionServer]: [Feedback] "dog." (9/9)
[splitWords_actionClient-2] [INFO] [1748999828.795498384] [splitWords_actionClient]: [Cliente][Feedback] Palabra actual: "dog."
[splitWords_actionServer-1] [INFO] [1748999829.795721212] [splitWords_actionServer]: [Success] Acción completada. Total de palabras: 9
[splitWords_actionClient-2] [INFO] [1748999829.797027041] [splitWords_actionClient]: [Cliente] Acción completada con éxito. Total de palabras: 9
[INFO] [splitWords_actionClient-2]: process has finished cleanly [pid 1248]
^C[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[INFO] [splitWords_actionServer-1]: process has finished cleanly [pid 1247]
```