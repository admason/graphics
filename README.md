# **Graphics Projects**
#### A collection of comnputer graphics projects
##### I have always been very interested in computer graphics and depictions of visual mathematics.
##### In fact the mystries of geometry triggered my interest in mathematics and remains my favourite field of maths.
##### The combination of maths and art is a passion I wish to persue, given enough time I hope to fill this repository with examples of my work.
## **1. Flowers.**
### Built on Python 3, jupyter notebook
#### flowers_1.ipynb
#### flowers_1.py


### **Build Status:** Working model, under development

#### This code uses the turtle module in order to draw geometric flowers.
#### The technique involves arclength measurements and the polyline function.
#### The user may choose the radius of the flower and the number of petals present via user inputs. Under the condition that there an ODD number of petals is selected. (This is due to undergo changes in further models to include even petals.)
#### For example, setting Radius=50 and Nuber of Petals=3, produces:
[![r50p3.jpg](https://i.postimg.cc/SxxWG0Cm/r50p3.jpg)](https://postimg.cc/BXRLqVmz)

#### To draw afresh, restart the Kernal and enter variables.
#### However, should you wish to add petals, rerun the code without interupting the kernal, and enter new variables.
#### Such as Radius=100, Number of Petals = 3.
[![r100p3.jpg](https://i.postimg.cc/xjL7wm7c/r100p3.jpg)](https://postimg.cc/9zFJTDch)

### How about number of petals?
#### Fixing Radius at 100, first 3 petals:
[![r100p3.jpg](https://i.postimg.cc/d1N1vXDj/r100p3.jpg)](https://postimg.cc/qhn0x1sN)
#### As before, no problems.
#### Next, keeping Radius at 100, this time 9 petals.
[![r100p3p5.jpg](https://i.postimg.cc/DfWs0dFw/r100p3p5.jpg)](https://postimg.cc/pyHy1jpw)
#### Notice how second flower with 9 petals has it's radius reduced?
#### Conviently it fits within the 3 petals, this is due to the division of 360 degree into 3 in the first drawing and then 9 in the second.
#### Thus the 360/9 fits within the 360/3 rotational symmetry.
#### But whay the reductio  in radius?
#### This is due to the code using arclength parametrisation, where step length is subject to division by 'n', the number of petals.
```
def arc(t, r, angle):
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length/n
    step_angle = float(angle)/n
    polyline(t, n, step_length, step_angle)
```
#### This is due for investigatio and will be improved in future versions. Perhaps a proportion may be applied to match the drawn radius to keep it consistent for the number of petals?

### **Tech** 
##### Coded with Python in Jupyter notebook turtle, math. 
##### Import Library List: 
##### Libaries initiated with code as:
```
import turtle
import math
```

## **Code**
```
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
```
