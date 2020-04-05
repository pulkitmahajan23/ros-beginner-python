#!/usr/bin/env python3

import rospy
from beginner_tutorials.msg import IoTsensor
import random

def iot_data_publisher():
    pub=rospy.Publisher('iot_sensor',IoTsensor,queue_size=10)
    rospy.init_node('iot_publisher',anonymous=True)
    rate=rospy.Rate(1)
    i = 0
    while not rospy.is_shutdown():
        iotsensor = IoTsensor()
        iotsensor.id = i #random id
        iotsensor.name = "iot_01" #random name
        iotsensor.temperature = 28.04 + random.random()*2 #random value
        iotsensor.humidity = 78.34 + random.random()*2    #random value
        rospy.loginfo("Publishing the values: ")
        rospy.loginfo(iotsensor)
        pub.publish(iotsensor)
        i=i+1
        rate.sleep()

if __name__ == "__main__":
    try:
        iot_data_publisher()
    except rospy.ROSInterruptException:
        pass

 