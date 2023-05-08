#!/usr/bin/env python
# license removed for brevity
import math
import rospy
from std_msgs.msg import Float64

def control():
    lpub1 = rospy.Publisher('/hmr/ljoint1_position_controller/command', Float64, queue_size=10)
    lpub2 = rospy.Publisher('/hmr/ljoint2_position_controller/command', Float64, queue_size=10)
    lpub3 = rospy.Publisher('/hmr/ljoint3_position_controller/command', Float64, queue_size=10)
    rpub1 = rospy.Publisher('/hmr/rjoint1_position_controller/command', Float64, queue_size=10)
    rpub2 = rospy.Publisher('/hmr/rjoint2_position_controller/command', Float64, queue_size=10)
    rpub3 = rospy.Publisher('/hmr/rjoint3_position_controller/command', Float64, queue_size=10)
    rospy.init_node('hmr_control', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        lposition1 = math.pi*(-557)/3600
        lposition2 = math.pi*39.38/180
        lposition3 = math.pi*(-11.53)/180
        rposition1 = math.pi*3.69/180
        rposition2 = math.pi*(26.31)/180
        rposition3 = math.pi*(-29.99)/180
        rospy.loginfo(lposition1)
        rospy.loginfo(lposition2)
        rospy.loginfo(lposition3)
        rospy.loginfo(rposition1)
        rospy.loginfo(rposition2)
        rospy.loginfo(rposition3)
        lpub1.publish(lposition1)
        lpub2.publish(lposition2)
        lpub3.publish(lposition3)
        rpub1.publish(rposition1)
        rpub2.publish(rposition2)
        rpub3.publish(rposition3)
        rate.sleep()

if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException:
        pass