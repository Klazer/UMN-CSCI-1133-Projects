#CSCI 1133 Section 19 Lab 006, HW4 Problem 1, Isaiah Herr

#==========================================
# Name: separate_int_and_str
# Purpose: Given a list of integer and strings, create two new lists. One
# list will contain the integers and the other list will contain the
# strings.
# Precondition: The list will only contain ints and strings
# Input Parameter(s)
# my_list: a list containing integers and strings
# Return Value(s)
# -- if the input parameter is an empty list , return a list
# with two empty lists: [ [ ], [ ] ]
# -- else return a list with the 0th index position containing the
# list of integers, and the 1st index position containing the
# list of strings. If there are no ints or strings, return
# an empty list in that position
#============================================

mylist = []
def separate_int_and_str(mylist):

    new_list = [x for x in mylist if isinstance(x, int)]
    new_list2 = [x for x in mylist if isinstance(x, str)]


    final_list = [new_list, new_list2]

    return final_list

#==========================================
# Name: average_of_lists
# Purpose: We want to the find the average of all
# lists within a single list and then list them out
# separately as integers
#
# Precondition: The list will only contain numbers
# Input Parameter(s): mylist
#
# Return Value(s): Elements that contain the averages of a list
# that was within the original list
# if nothing, return a [].
#
#============================================

def average_of_lists(mylist):

    newlist = []
    
    if mylist == []:
        return []
      
    if isinstance(mylist[0], int) or isinstance(mylist[0], float):
            result = round(sum(mylist)/len(mylist))
            newlist.append(result)
    else:
        for x in mylist:
            if x == []:
                newlist.append(x)
            else:
                result = round(sum(x)/len(x))
                newlist.append(result)

    return newlist

#==========================================
# Name: min_of_list
# Purpose: Find the smallest or minimum number from multiple lists
# Precondition: The list will only contain numbers
# Input Parameter(s): my_list
#
# Return Value(s): The smallest valued number
# from all the list elements.
# If the list is empty, return a 0
#
#============================================

def min_of_list(mylist):

    if mylist == []:
        return 0
    elif mylist == [[]]:
        return 0
    
    for x in range(len(mylist)):
        if mylist[x] == []:
            mylist[x] = [0]
        mylist[x].sort()
    mylist.sort()

    if mylist[0] == []:
        return 0
    else: 
        return mylist[0][0]


#==========================================
# Name: greater_than
# Purpose: Compare values within a list element with a
# second element consisting of a single integer.
# We want to return True, if all numbers within the list
# are greater than the second element and false if not.

# Precondition: The list will only contain numbers
# Input Parameter(s): mylist, x
#
# Return Value(s): True if all numbers within the
# list element is greater than the second element
# or False if not.
#
#============================================

def greater_than(mylist, x):

    if mylist == []: #If nothing is in the list, it will be true 
        return True
    elif len(mylist) == 0:
        return True
    
    
    for y in mylist: #Checks to see if any values in mylist
        if y > x:          #are greater than x
            return True
        elif y <= x:
            return False

    
#==========================================
# Name: selection_sort
# Purpose: We want to sort a list of numbers in ascending
# order without using the built in sort functions or anything
# that could index the list for us.
#
# Precondition: The list will only contain numbers
# Input Parameter(s): my_list
#
# Return Value(s): The original list, but sorted in
# ascending order (from 1,2,3, etc.)
#
#============================================

def selection_sort(mylist):

    for x in range(len(mylist)):
        for y in range(x+1, len(mylist)):
            if mylist[x] > mylist[y]:
                mylist[x], mylist[y] = mylist[y], mylist[x]



