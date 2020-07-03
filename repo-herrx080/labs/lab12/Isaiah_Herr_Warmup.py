import turtle
myt = turtle.Turtle()
scr = turtle.Screen() #Brings up turtle window
scr.delay

scr.delay(0) #Sets delay to 0 to make it as fast as possible
scr.delay()

myt.speed()

myt.speed(0) #Set speed drawing to 0 to make it as fast as possible
myt.speed()

myt.hideturtle()
myt.penup() #Lifts 'pen' off of turtle
myt.goto(40,40) #Coordinates where cirlce will be located
myt.circle(100)
myt.pendown() #Puts pen back down to draw on turtle
myt.circle(100) #Draws circle
myt.fillcolor("green") #Indicates which color to fill circle with

myt.begin_fill() #Fills in colors at specified circle
myt.circle(100)
myt.end_fill()
myt.penup()
myt.goto(-50, -50)
myt.pendown()
myt.fillcolor("blue")
myt.begin_fill()
for i in range(4): #Creates rectangle
    myt.forward(100)
    myt.right(90)

myt.end_fill()


def mouseInput(x,y): #Use for the onclick function to print x and y coordinates
	print(x, ',', y)

	
scr.onclick(mouseInput) #Makes it so that when we click on turtle screen, prints coordinates
scr.listen() #I guess it prints out current coordinates?
243.0 , -352.0
