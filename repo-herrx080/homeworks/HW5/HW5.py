#CSCI 1133 Section 19 Lab 006, Homework Problem 1, Isaiah Herr, herrx080

#==========================================
# Name: cnt_occur(mylist, val)
#
# Purpose: Counts the amout of times val, the desired number, appears
# in the list or list of lists.
#
# Precondition: Must contain either integers or strings in the list or
# list of lists. The list may also be empty
#
# Input Parameter(s): mylist (Input parameter list containing all values),
# val (desired value that we want to count to see how many of this value
# is in the list)
#
# Return Value(s): An integer that represents the amount of times the element
# appears within the list
#============================================

def cnt_occur(mylist, val):
    
    if len(mylist) == 0: #Basecase for an empty list
        return 0
    
    if isinstance(mylist[0], list):  #Checks to see if element is a list or not and
        return cnt_occur(mylist[0], val) + cnt_occur(mylist[1:], val) #recalls function to account for this
    
    elif mylist[0] == val: #Adds a count of 1 if this is true
        return 1 + cnt_occur(mylist[1:], val)
    
    else: 
        return cnt_occur(mylist[1:], val)



#CSCI 1133 Section 19 Lab 006, Homework Problem 2, Isaiah Herr, herrx080

#==========================================
# Name: position(mylist, val)
#
# Precondition: Cannot do any form of looping.
# There are no embedded lists within the list that is inputted
#
# Input Parameter(s): mylist (list that is being inputted), val (desired number)
#
# Return Value(s): All the indexes of the desired number that is inputted
# if the number exists within the list. This is done by returning the helper
# Function, which keeps track of the indexes. If there's nothing, it returns an empty list
#============================================

def position(mylist, val):
    newlist = [] #Contains list outside of helper function so that it is
    count = 0 #not changed back to an empty list after every recursive call
    return helper1(newlist, mylist, val, count)

#==========================================
# Name: helper1(1newlist, mylist, val, count)
# Purpose: Helps the main function in determining all the positions
# of the desired value as set in the input parameters.
# Precondition: There are no embedded lists within the inputted list
# Cannot do any looping
#
# Input Parameter(s): newlist (new list that will contain all the
# indexes that will be returned), mylist (list in the input parameter),
# val (the desired number that we want the positions of),
# count(keeps track of the indexes of val)
#
# Return Value(s): Should return the newlist if the count reaches the
# length of mylist.
# Also returns/recalls the helper function again which continues
# Until the count reaches the length of mylist
#============================================

def helper1(newlist, mylist, val, count):
    if len(mylist) == 0: #Basecase if empty list, still returns an empty list
        return newlist
    elif count >= len(mylist): #Ends the function if this is true
        return newlist

    if mylist[count] == val:
        newlist.append(count)
        return helper1(newlist, mylist, val, count+1)    #Recalls the function again
                                         #While also incerasing count by 1
    else:
        return helper1(newlist, mylist, val, count+1)



#CSCI 1133 Section 19 Lab 006, Homework Problem 3, Isaiah Herr, herrx080


#==========================================
# Name: rm_conseq_dups(mylist)
#
# Purpose: Keeps the newlist as a more global variable so that it can be updated
# by the helper function. Also calls the helper function which will then return a list
# removing consecutive numbers that are adjacent to the original.
#
# Precondition: There will be no embedded lists.
# Either strings or integers will be in the list
# List may also be empty
#
# Input Parameter(s): mylist, This is the list that is inputted by the user
# Return Value(s): A new list containing all previous values, but any values
# That are the consecutive and adjacent are removed except for the original element.
# Also returns/recalls the helper function which returns the new list.
#============================================


def rm_conseq_dups(mylist):
    newlist = []
    return helper2(newlist, mylist)


#==========================================
# Name: helper2(newlist, mylist)
# Purpose: It plays the main role in deleting any consecutive elements
# That are the same and adjacent to each other
#
# Precondition: No embedded lists and contains either integers or strings
# May also have an empty list as an input parameter
#
# Input Parameter(s): newlist (New list that will be returned will all adjacent
# consecutive values removed), mylist (Original list containing values, or strings)
# Return Value(s): Returns the new list with consecutive numbers/string that are adjacent
# removed. Also returns/recalls the helper function again to go through each element
# separately after checking if the number in front of it is the same.
#============================================

def helper2(newlist, mylist):
    if len(mylist) == 0:    #Basecase if parameter is an empty list, still returns an empty list 
        return newlist
    elif len(mylist) == 1:      #Adds last value to list then returns the list
        newlist.append(mylist[0])
        return newlist
    
    if mylist[0] != mylist[1]:      #Adds value onto list as long as the number in front
        newlist.append(mylist[0])   # isn't the same
        return helper2(newlist, mylist[1:])#Use the original list to concantenate the recursion.
    else:                                   #Ex) mylist[0] + mylist[1:]
        return helper2(newlist, mylist[1:])


#CSCI 1133 Section 19 Lab 006, Homework Problem 4, Isaiah Herr, herrx080

#==========================================
# Name: sequence(n)

# Purpose: Contains a new empty list that will the values
# from the sequence starting at three.
# Also contains Count which keeps track of which position a certain
# value is at in the helper function.
#
# Precondition: Cannot use any looping or iteration
# Sequence must start at 3
# Input parameter will always be an integer
#
# Input Parameter(s): n (integer which asks for the value in the list
# at position n)
#
# Return Value(s): The helper function is returned which then also returns
# the value in the sequence at position n.
#============================================

def sequence(n):
    newlist = []
    count = 0
    return helper3(count, newlist, n)


#==========================================
# Name: helper3(count, newlist, n)
# Purpose: Contains the instructions that calcualte the equation for the
# Sequence while also keeping track of the count, which is the position of
# The value in the list. Adds values into the list until count equals
# The inputted value of n.
#
# Precondition: Cannot use any looping or iteration
# Must have the sequence start at 3
# Must have an empty list to add values from the equation into.
#
# Input Parameter(s): count (Keeps track of the position of the value
# in the sequence), newlist (Contains all values in the sequence),
# n (the desired position that is being asked for in the input parameter.
# Count must equal n to stop the function)
#
# Return Value(s): A value from the new list that is returned
# Depending on what type of number count is.
# Also returns the helper function again to add the count until it equals n
# and also to update the new list with values.
#============================================

def helper3(count, newlist, n):
    equation = 3*2**count #Equation used to calculate values in the sequence

    if n == 0 or n == 1: #Base case
        return 3
    elif count == n: #If count = n, the input parameter, count is subtracted by
                        #1 to match n and added to equation and added onto list
        count = count - 1
        newlist.append(equation)
        return newlist[count]
    else:
        newlist.append(equation) #Continually adds values to the list
                                #until we reach the base case
        return helper3(count+1, newlist, n)




#CSCI 1133 Section 19 Lab 006, Homework Problem 5, Isaiah Herr, herrx080

#==========================================
# Name: rangeIt(x,y)
#
# Purpose: Contains the newlist which can be continually updated by the helper
# function. Returns the helper function to give an output of the newlist containing
# The range of numbers from x to y.
#
# Precondition: Must be two integers
# x must always be the same or smaller than y
#
# Input Parameter(s): x (smaller value), y (larger value)
# Return Value(s): Returns the helper function that contains a new list
# that has all the numbers from the range of
#============================================

def rangeIt(x,y):
    newlist = []
    return helper4(x, y, newlist)

#==========================================
# Name: helper4(x, y, newlist)

# Purpose: Contains the instructions that creates a new list containing
# all numbers from the range of x to y via recursion.
#
# Precondition: Must be two integers
# x must always be the same or be smaller than y
#
# Input Parameter(s): x (smaller number), y (larger number),
# newlist (Empty list that will contain numbers from x to y)
#
# Return Value(s): A new list containing values from x to y will be
# returned. The helper function will also be returned/recalled
# in order to continue to add numbers (x) to newlist until x is equal to y.
#============================================

def helper4(x, y, newlist):
    if x == y: #Adds the last value of x onto list and returns the list, basecase
        newlist.append(x)
        return newlist
    else:
        newlist.append(x) #Continually adds x onto list until basecase
        return helper4(x+1, y, newlist)

