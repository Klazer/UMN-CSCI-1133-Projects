#CSCI 1133 Section 19 Lab 006, Stretch, Isaiah Herr

import turtle #always import outside of functions

#1
def randColor():
    import random    
    colors = ["red", "yellow", "green", "blue", "purple", "orange"]

    return random.choice(colors) #Returns a random color from the list

#2
class Shape: #Parent class that Circle will inherit from
    def __init__(self, x = 0, y = 0, color = "", fill = False): #constructor
        self.x = int(x)
        self.y = int(y)
        self.color = color
        self.fill = fill

    def setFillercolor(self, color): #Sets color to color defined in parameter
        self.color = str(color)

    def setFilled(self, fill):
        self.fill = bool(fill)

    def isFilled():
        return self.fill

#3
class Circle(Shape):
    def __init__(self, x = 0, y = 0, color = "", fill = False, radius = 1):
        Shape.__init__(self, x, y, color, fill)
        self.radius = radius

    def draw(self, turtle):
        turtle.speed(0)
        
        if self.fill == True:
            turtle.penup()
            turtle.goto(self.x, self.y)
            turtle.circle(self.radius)
            turtle.pendown()
            turtle.circle(self.radius)
            turtle.fillcolor(self.color)
            turtle.begin_fill()
            turtle.circle(self.radius)
            turtle.end_fill()

        elif self.fill == False:
            turtle.penup()
            turtle.goto(self.x, self.y)
            turtle.circle(self.radius)
            turtle.pendown()
            turtle.circle(self.radius)
