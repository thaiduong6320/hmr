#!/usr/bin/env python
import math
import rospy
from std_msgs.msg import Float64
import time
import csv

def main():
    lpub1 = rospy.Publisher('/hmr/ljoint1_position_controller/command', Float64, queue_size=10)
    lpub2 = rospy.Publisher('/hmr/ljoint2_position_controller/command', Float64, queue_size=10)
    lpub3 = rospy.Publisher('/hmr/ljoint3_position_controller/command', Float64, queue_size=10)
    rpub1 = rospy.Publisher('/hmr/rjoint1_position_controller/command', Float64, queue_size=10)
    rpub2 = rospy.Publisher('/hmr/rjoint2_position_controller/command', Float64, queue_size=10)
    rpub3 = rospy.Publisher('/hmr/rjoint3_position_controller/command', Float64, queue_size=10)
    
    rospy.init_node('hmr_control', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        with open('/home/dev/hmr_ws/src/hmr/hmr_description/src/pose.csv', 'r') as csvfile:
            spamreader = csvfile.read().split('\n')
            i = 0
            
            for row in spamreader:
                if i<7 :
                    q_set = row.split(',')
                    lp1 = q_set[1][0]
                    lp2 = q_set[1][1]
                    lp3 = q_set[1][2]
                    rp1 = q_set[1][3]
                    rp2 = q_set[1][4]
                    rp3 = q_set[1][5]

                    lpub1.publish(lp1)
                    lpub2.publish(lp2)
                    lpub3.publish(lp3)
                    rpub1.publish(rp1)
                    rpub2.publish(rp2)
                    rpub3.publish(rp3)
                    time.sleep(1)
                    i = i + 1
                if i==7 :
                    time.sleep(5)
                time.sleep(0.2)
        time.sleep(5)
        lpub1.publish(0)
        lpub2.publish(0)
        lpub3.publish(0)
        rpub1.publish(0)
        rpub2.publish(0)
        rpub3.publish(0)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass