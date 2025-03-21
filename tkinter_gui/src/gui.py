#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Float32MultiArray
from geometry_msgs.msg import Twist
from tkinter import *
import time


global direction
global message

velocity = Twist()
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10) 

def callback(received):
    global message
    message_text = "Battery charge: " + str(received.data[0]) + "%, Rover speed: " + str(received.data[1]) + " m/s, Latency: " + str(received.data[2]) + " ms"
    message.config(text=message_text)
    print(received.data)

rospy.Subscriber("/rover_stats", Float32MultiArray, callback)
   
def stop(e):
    global message
   
    
        
    
    velocity.linear.x = 0.0
    velocity.linear.y = 0.0
    velocity.linear.z = 0.0
    velocity.angular.z = 0.0
    pub.publish(velocity)
def forward(e):
    
    velocity.linear.x = 1.0
    velocity.linear.y = 0.0
    velocity.linear.z = 0.0
    pub.publish(velocity)
def left(e):
    
    velocity.angular.z = 1.0
    velocity.linear.y = 0.0
    velocity.linear.z = 0.0
    pub.publish(velocity)
def right(e):
    
    velocity.angular.z = -1.0
    velocity.linear.y = 0.0
    velocity.linear.z = 0.0
    pub.publish(velocity)
def back(e):
    
    velocity.linear.x = -1.0
    velocity.linear.y = 0.0
    velocity.linear.z = 0.0
    pub.publish(velocity)
    

def command():
    rospy.init_node("command_node", anonymous=True)
    rate = rospy.Rate(10)
    
    
    root = Tk()
    root.title("GUI for Turtlebot")
    root.geometry("900x600")
    frame1 = Frame(root)
    frame1.grid(row=0, column=0,)
    warning = Label(frame1, text="PRESS THE BUTTONS TO MOVE THE BOT")
    warning.grid(row=0, column=1, padx=5, pady=5)
    button = Button(frame1, text='Front')
    button.grid(row=1, column=1, pady=10)
    button.bind('<ButtonPress-1>',forward)
    

    button2 = Button(frame1, text='Left')
    button2.grid(row=2, column=0, pady=10)
    button2.bind('<ButtonPress-1>',left)
    

    button5= Button(frame1, text='Stop')
    button5.grid(row=2, column=1, pady=10)
    button5.bind('<ButtonPress-1>',stop)

    button3 = Button(frame1, text='Right')
    button3.grid(row=2, column=2, pady=10)
    button3.bind('<ButtonPress-1>',right)
    


    button4 = Button(frame1, text='Back')
    button4.grid(row=3, column=1, pady=10)
    button4.bind('<ButtonPress-1>',back)
    
    
    frame2 = Frame(root)
    frame2.grid(row=0, column=1)
    
  
    global message
    message = Label(frame2, borderwidth=1)
    message.grid(row=2, column=0, columnspan=2, padx=(40,0), pady=10)
    root.mainloop()
    
if __name__=='__main__':
    command()