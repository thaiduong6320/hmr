#include "ros/ros.h"
#include "std_msgs/Float64.h"

#include <sstream>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "control");

  ros::NodeHandle nh;

  ros::Publisher lpub1 = nh.advertise<std_msgs::Float64>("/hmr/ljoint1_position_controller/command", 1000);
  ros::Publisher lpub2 = nh.advertise<std_msgs::Float64>("/hmr/ljoint2_position_controller/command", 1000);
  ros::Publisher lpub3 = nh.advertise<std_msgs::Float64>("/hmr/ljoint3_position_controller/command", 1000);
  ros::Publisher rpub1 = nh.advertise<std_msgs::Float64>("/hmr/rjoint1_position_controller/command", 1000);
  ros::Publisher rpub2 = nh.advertise<std_msgs::Float64>("/hmr/rjoint2_position_controller/command", 1000);
  ros::Publisher rpub3 = nh.advertise<std_msgs::Float64>("/hmr/rjoint3_position_controller/command", 1000);

  ros::Rate loop_rate(10);

  while (ros::ok())
  {
 
    std_msgs::Float64 lmsg1;
    std_msgs::Float64 lmsg2;
    std_msgs::Float64 lmsg3;
    std_msgs::Float64 rmsg1;
    std_msgs::Float64 rmsg2;
    std_msgs::Float64 rmsg3;

    lmsg1.data = 3.141592654*(-557)/3600;
    lmsg2.data = 3.141592654*39.38/180;
    lmsg3.data = 3.141592654*(-11.53)/180;
    rmsg1.data = 3.141592654*3.69/180;
    rmsg2.data = 3.141592654*(26.31)/180;
    rmsg3.data = 3.141592654*(-29.99)/180;

    ROS_INFO("%s", lmsg1.data.c_str());
    ROS_INFO("%s", lmsg2.data.c_str());
    ROS_INFO("%s", lmsg3.data.c_str());
    ROS_INFO("%s", rmsg1.data.c_str());
    ROS_INFO("%s", rmsg2.data.c_str());
    ROS_INFO("%s", rmsg3.data.c_str());
     
    lpub1.publish(lmsg1);
    lpub2.publish(lmsg2);
    lpub3.publish(lmsg3);
    rpub1.publish(rmsg1);
    rpub2.publish(rmsg2);
    rpub3.publish(rmsg3);

    ros::spinOnce();

    loop_rate.sleep();

  }


  return 0;
}