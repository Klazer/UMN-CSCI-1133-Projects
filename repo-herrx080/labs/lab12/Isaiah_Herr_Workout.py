#CSCI 1133 Section 19 Lab 006, Workout, Isaiah Herr

import turtle
import random

#1
def randColor():   
    colors = ["red", "yellow", "green", "blue", "purple", "orange"]

    return random.choice(colors) #Returns a random color from the list


import turtle
import random
class Display:
    def __init__(self, myt=turtle.Turtle(), scr=turtle.Screen()):
        self.myt = myt
        self.scr = scr

    def mouseEvent(x,y):
        radius = random.randint(10, 100)
        color = randColor()    

        self.myt.penup()
        self.myt.goto(x, y)
        self.myt.circle(radius)
        self.myt.pendown()
        self.myt.circle(radius)
        self.myt.fillcolor(randColor())
        self.myt.begin_fill()
        self.myt.circle(radius)
        self.myt.end_fill()
