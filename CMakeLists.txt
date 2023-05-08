cmake_minimum_required(VERSION 2.8.3)

project(hmr)

find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
  roscpp
  std_msgs
  rospy
  message_generation 
  genmsg
  robot_state_publisher
  gazebo_ros_control
  forward_command_controller
  hardware_interface
  pluginlib
  roslaunch
)
## Declare ROS messages and services

## Generate added messages and services
generate_messages(DEPENDENCIES std_msgs)
catkin_package(
    DEPENDS
      gazebo_ros
    CATKIN_DEPENDS
    INCLUDE_DIRS
    LIBRARIES
)
include_directories(include ${catkin_INCLUDE_DIRS} ${GAZEBO_INCLUDE_DIRS} ${SDFormat_INCLUDE_DIRS})

add_executable(main hmr_description/src/main.cpp)
target_link_libraries(main ${catkin_LIBRARIES})
# add_dependencies(talker beginner_tutorials_generate_messages_cpp)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

install(DIRECTORY meshes
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

install(DIRECTORY urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})