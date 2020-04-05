#!/usr/bin/env python3

import rospy
from beginner_tutorials.msg import IoTsensor

def iot_sensor_callback(iot_sensor_message):
    rospy.loginfo("Data received: (%d %s %.2f %.2f)",
    iot_sensor_message.id, iot_sensor_message.name,
    iot_sensor_message.temperature, iot_sensor_message.humidity)

rospy.init_node("iot_subscriber", anonymous=True)
rospy.Subscriber('iot_sensor_receive',IoTsensor,iot_sensor_callback)
rospy.spin()

