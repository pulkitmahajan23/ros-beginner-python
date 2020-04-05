#!/usr/bin/env python

from beginner_tutorials.srv import AddTwoInt
from beginner_tutorials.srv import AddTwoIntRequest
from beginner_tutorials.srv import AddTwoIntResponse

import rospy

def handle_add_two_int(req):
    print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a+req.b))
    return AddTwoIntResponse(req.a+req.b)

def add_two_int_server():
    rospy.init_node('add_two_int_server')
    s=rospy.Service('add_two_ints',AddTwoInt, handle_add_two_int)
    print "Ready to add two ints"
    rospy.spin()

if __name__ == "__main__":
    add_two_int_server()