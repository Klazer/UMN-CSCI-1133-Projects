#CSCI 1133 Section 19 Lab 006, Homework Problem B, Isaiah Herr

import turtle
turtle.showturtle

def main():
    lengthOfSide = float(input("Please enter the length of the side you want the star to be: "))
    fourSidedStar(lengthOfSide)

def fourSidedStar(lengthOfSide):
    turtle.left(75)
    
    i = 0
    while(i < 4):
        turtle.forward(lengthOfSide)
        turtle.right(60)
        turtle.forward(lengthOfSide)
        turtle.left(150)
        i = i+1

main()
