#!/usr/bin/env python
# license removed for brevity
import math
import rospy
from std_msgs.msg import Float64

def talker():
    pub = rospy.Publisher('/rrbot/joint1_position_controller', Float64, queue_size=10)
    rospy.init_node('rrbot_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        position = math.sin(i)
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()
        i += 0.01

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass