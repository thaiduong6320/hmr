#!/usr/bin/env python
# license removed for brevity
import math
import rospy
from std_msgs.msg import Float64
import time

def control():
    lpub1 = rospy.Publisher('/hmr/ljoint1_position_controller/command', Float64, queue_size=10)
    lpub2 = rospy.Publisher('/hmr/ljoint2_position_controller/command', Float64, queue_size=10)
    lpub3 = rospy.Publisher('/hmr/ljoint3_position_controller/command', Float64, queue_size=10)
    rpub1 = rospy.Publisher('/hmr/rjoint1_position_controller/command', Float64, queue_size=10)
    rpub2 = rospy.Publisher('/hmr/rjoint2_position_controller/command', Float64, queue_size=10)
    rpub3 = rospy.Publisher('/hmr/rjoint3_position_controller/command', Float64, queue_size=10)
    
    q_set = [[-0.34906, 0.69813, -0.34906, -0.34906, 0.69813, -0.34906],
             [-0.523598, 0.34906, -0.34906, -0.523598, 0.34906, -0.34906]]
    rospy.init_node('hmr_control', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    def post(q):
        lpub1.publish(q[0])
        lpub2.publish(q[1])
        lpub3.publish(q[2])
        rpub1.publish(q[3])
        rpub2.publish(q[4])
        rpub3.publish(q[5])
        time.sleep(1)

    while not rospy.is_shutdown():
        # rospy.loginfo(lpub1)
        # rospy.loginfo(lpub2)
        # rospy.loginfo(lpub3)
        # rospy.loginfo(rpub1)
        # rospy.loginfo(rpub2)
        # rospy.loginfo(rpub3)
        time.sleep(1)
        lpub1.publish(0)
        lpub2.publish(0)
        lpub3.publish(0)
        rpub1.publish(0)
        rpub2.publish(0)
        rpub3.publish(0)
        time.sleep(1)
        lpub1.publish(-0.25)
        lpub2.publish(0.5)
        lpub3.publish(-0.25)
        rpub1.publish(-0.25)
        rpub2.publish(0.5)
        rpub3.publish(-0.25)
        # rate.sleep()

if __name__ == '__main__':
    control()