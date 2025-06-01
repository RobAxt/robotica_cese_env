cmake_minimum_required(VERSION 3.5)
project(axt_ejer2_pkg)

# 1. Encontrar dependencias
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# 2. Indicar que generemos las clases para la acción SplitWords
rosidl_generate_interfaces(${PROJECT_NAME}
  "action/SplitWords.action"
)

# 3. Exportar dependencias de runtime para que Python encuentre el módulo generado
ament_export_dependencies(rosidl_default_runtime)

# 4. No definimos código C++; el nodo Python se instala con setup.py, pero
#    ROS 2 necesita este CMakeLists.txt para invocar rosidl.
ament_package()
