import csv
import time
from std_msgs.msg import Float64
import rospy
with open('/home/dev/hmr_ws/src/hmr/hmr_description/src/pose.csv', 'r') as csvfile:
    spamreader = csvfile.read().split('\n')
    i = 0
    for row in spamreader:
        if i<7 :
            q_set = row.split(',')
            f =[]
            for item in q_set:
                f.append(Float64(item))
            lp1 = type(f[0])
            lp2 = type(f[1])
            lp3 = type(f[2])
            rp1 = type(f[3])
            rp2 = type(f[4])
            rp3 = type(f[5])

            print(lp1)
            print(lp2)
            print(lp3)
            print(rp1)
            print(rp2)
            print(rp3)
            time.sleep(1)
            i = i + 1
        if i==7 :
            time.sleep(5)
        time.sleep(0.2)


# with open('/home/dev/hmr_ws/src/hmr/hmr_description/src/pose.csv', 'r') as csvfile:
#     spamreader = csv.reader(csvfile)
#     i = 0
#     for row in spamreader:
#         if i<7 :
#             q_set = row
#             q0 = (float, q_set[0])
#             q1 = (float, q_set[1])
#             q2 = (float, q_set[2])
#             q3 = (float, q_set[3])
#             q4 = (float, q_set[4])
#             q5 = (float, q_set[5])
#             print(q0)
#             print(q1)
#             print(q2)
#             print(q3)
#             print(q4)
#             print(q5)
#             print('__')
#             time.sleep(1)
#             i = i + 1
#         if i==7 :
#             time.sleep(5)
#         time.sleep(0.2)

# with open('/home/dev/hmr_ws/src/hmr/hmr_description/src/pose.csv', 'r') as csvfile:
#     spamreader = csvfile.read().split('\n')
#     i = 0
#     for row in spamreader:
#         q_set = (float, row.split(','))
#         q = q_set[1][1]
#         print(q)
#         i = i + 1
#         if i==7 :
#             time.sleep(5)
#         time.sleep(0.2)