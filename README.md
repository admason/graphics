# **Graphics Projects**
#### A collection of computer graphics projects
##### I have always been very interested in computer graphics and depictions of visual mathematics.
##### In fact the mystries of geometry triggered my interest in mathematics and remains my favourite field of maths.
##### The combination of maths and art is a passion I wish to persue, given enough time I hope to fill this repository with examples of my work.
## **1. Flowers with turtle.**
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
#### But why the reduction  in radius?
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
# **2. Vector Rotation**
## 
### Built on Python 3, jupyter notebook
#### Vector_rotation.ipynb
#### This code take the input as the x,y elements of a vector in R^2 cartesian space and apply a rotation based upon the vector's angle with the line y=0. 


### **Build Status:** Working model, under development

### **Tech** 
##### Coded with Python in Jupyter notebook matplotlib.pyplot, numpy, math. 
##### Import Library List: 
##### Libaries initiated with code as:
```
import numpy as np
import math as m
import matplotlib.pyplot as plt
```

## **Code**

# Define the vector

```
import numpy as np
import math as m
x=float(input('Enter x coord: ' ))
y=float(input('Enter y coord: ' ))
a = np.array([x,y])
v = np.transpose(a)
print('a = {}, v = {}, vector v =[{}, {}]'.format(a,v, v[0],v[1]))
```
# Execute code 
```
# To plot the vector
import matplotlib.pyplot as plt
ax = plt.axes()
plt.axis([-1-v[0],1+v[0],-1-v[1],1+v[1]])
x1 = 0
y1 = 0
x2 = v[0]
y2 = v[1]

ax.arrow(0,0,v[0],v[1], head_width=0.09, head_length=0.09, fc = 'y', ec ='k')

plt.text(v[0]*1.3,v[1]*1.3,'$X$', fontsize=15)

plt.show()
grad = (y2 - y1)/(x2 - x1)
print('gradient: {}'.format(grad))
```
# Execute

```
# Rotation Operator
thetadeg = np.round(m.degrees(m.atan(y/x)),12)

thetarad = np.round(m.atan(y/x),12)

print('Angle of rotatation is {} degrees or {} radians'.format(thetadeg,thetarad))
```
# Execute

```
R=np.array([[np.cos(thetarad), -np.sin(thetarad)],[np.sin(thetarad), np.cos(thetarad)]])
print(R)
# Rotated vector B=A*X
B=np.dot(R,v)
print(B)
```
# Execute

```
# Plot both vectors

import matplotlib.pyplot as plt

ax = plt.axes()
plt.axis([-2-max(v[0],B[0]),2+max(v[0],B[0]),-2-max(v[1],B[1]),2+max(v[1],B[1])])


ax.arrow(0,0,v[0],v[1], head_width=0.09, head_length=0.09, fc = 'y', ec ='k')
ax.arrow(0,0,B[0],B[1], head_width=0.1, head_length=0.1, fc = 'k', ec = 'k')

plt.text(v[0]*1.3,v[1]*1.3,'$v$', fontsize=15)
plt.text(B[0]+0.2,B[1],'$B=Rv$', fontsize=15)

plt.show()
```
# Execute

## **Improvements:**

### Condense the code into on cell.
### Incorporate into a GUI for ease of use.
### Options for calculating the Orthoganal vector
### Expand the code into 3Dimension, or further in 4+ dimensional Tensor
