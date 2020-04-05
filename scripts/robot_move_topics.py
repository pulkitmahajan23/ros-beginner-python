#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move():
    speed_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rospy.init_node('movement',anonymous=True)
    rate=rospy.Rate(1)
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 1.0
        twist.linear.y = 2.0
        twist.linear.z = 0.0
        twist.angular.x = 2.0
        twist.angular.y = 1.0
        twist.angular.z = 0.0
        speed_publisher.publish(twist)
        rate.sleep()

if __name__ == "__main__":
    try:
        move()
    except rospy.ROSInterruptException:
        pass

 