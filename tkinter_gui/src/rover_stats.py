#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Float32MultiArray

class rover_stats:
    def __init__(self) -> None:
        rospy.init_node("rover_stats", anonymous=True)
        self.pub = rospy.Publisher('/rover_stats', Float32MultiArray, queue_size=10)
        
        
    def send(self, message):
        self.pub.publish(Float32MultiArray(data=message))
        rospy.loginfo(message)
    def run(self):
        rospy.loginfo("Message node is running")
        while not rospy.is_shutdown():
            message = [90.0, 1.0, 500.0]
            self.send(message)
            rospy.sleep(1)
if __name__=='__main__':
    node = rover_stats()
    node.run()
    