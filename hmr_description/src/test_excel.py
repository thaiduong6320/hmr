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
        with open('/home/dev/hmr_ws/src/hmr/hmr_description/src/data3.csv', 'r') as csvfile:
            spamreader = csvfile.read().split('\n')
            i = 0
            
            for row in spamreader:
                if i<202 :
                    q_set = row.split(',')
                    f =[]
                    for item in q_set:
                        f.append(float(item))
                    lp1 = (f[0])
                    lp2 = (f[1])
                    lp3 = (f[2])
                    rp1 = (f[3])
                    rp2 = (f[4])
                    rp3 = (f[5])

                    lpub1.publish(lp1)
                    lpub2.publish(lp2)
                    lpub3.publish(lp3)
                    rpub1.publish(rp1)
                    rpub2.publish(rp2)
                    rpub3.publish(rp3)
                    # time.sleep(0.01)
                    i = i + 1
                if i==202 :
                    time.sleep(0.2)
                time.sleep(0.2)
        # time.sleep(5)
        # lpub1.publish(0)
        # lpub2.publish(0)
        # lpub3.publish(0)
        # # rpub1.publish(0)
        # # rpub2.publish(0)
        # # rpub3.publish(0)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass