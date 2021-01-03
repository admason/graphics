#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Flowers with odd numbers of petal

import turtle
import math

r=int(input("Radius of flower? "))
n=int(input("Number of petals, (odd numbers only)? "))

angle=360/n

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
bloom=turtle.Turtle()

def arc(t, r, angle):
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length/n
    step_angle = float(angle)/n
    polyline(t, n, step_length, step_angle)

bloom=turtle.Turtle()

def polygon(t, n, length):
    angle = 360/n
    polyline(t, n, length, angle)

def petal(t,r,angle):
    angle=360/n
    arc(t,r,angle)
    t.lt(180-angle)
    arc(t,r,angle)


def flower(t,r,n,angle):
    for i in range(n):
        petal(t,r,angle)
        t.rt(180-angle)
    
flower(bloom,r,n,angle)


# In[ ]:




