#CSCI 1133 Section 19 Lab 006, Problem A, Isaiah Herr, herrx080

import time
class StopWatch:

#==========================================
# Name: def __init__(self, start = 0, end = 0)

# Purpose: The constructor for the class. It defines what variables
# should be passed in for data type StopWatch and defaults the start and
# end variables to 0 if nothing is specified

# Precondition: Both the start and end variables must be numerical
# values or can be a function that records the time such as the time.time()
# function. Must also import time into the code before running anything.

# Input Parameter(s): start(Numerical value that represents when the
# stopwatch starts), end(Numerical value that represents when stopwatch
# ends)

# Return Value(s): Nothing, should define both self._start and self._end
# as the time.time() function.
#============================================

    def __init__(self, start = 0, end = 0): #Constructor, assigns self to 
        self._start = time.time() #both the start and end variables
        self._end = time.time()

#==========================================
# Name: get_start(self)

# Purpose: returns the value stored in self._start

# Precondition: needs the input parameter self, or the name of the variable
# containing data type of StopWatch

# Input Parameter(s): self(input parameter that allows us to call other
# variables containing self. as defined in other functions. Also allows
# us to call variables containing data type StopWatch)

# Return Value(s): A numerical value that was recorded by time.time()
# when an object of data type StopWatch was created or the numerical value
# recorded by a different function such as set_start
#============================================
    def get_start(self):
        return self._start

#==========================================
# Name: get_end(self)

# Purpose: returns the value stored in self._end

# Precondition: needs the input parameter self, or the name of the variable
# containing data type of StopWatch. Must also import time.

# Input Parameter(s): self(input parameter that allows us to call other
# variables containing self. as defined in other functions. Also allows
# us to call variables containing data type StopWatch)

# Return Value(s): A numerical value that was recorded by time.time()
# when an object of data type StopWatch was created or the numerical value
# recorded by a different function such as set_end
#============================================

    def get_end(self):
        return self._end

#==========================================
# Name: current_time()

# Purpose: Returns the current local time in the military time format

# Precondition: Must import
# Input Parameter(s): N/A
# Return Value(s): The current local time in the military time format
#============================================

    def current_time():
        return time.strftime('%H:%M:%S') #Returns local time using
                            #strftime. It is formatted within the parenthesis

#==========================================
# Name: set_start(self)
# Purpose: Gives the self._start variable a new numerical value containing
# the current time in seconds.

# Precondition: Must import time and have the input parameter self,
# or a variable containing a data type StopWatch

# Input Parameter(s): self(Input parameter that allows you to use
# variables containing self. as defined from other functions. May also be
# the variable containing an object of data type StopWatch)

# Return Value(s): Nothing, sets self._start to a new value
#============================================
    def set_start(self): #Sets start to a new numerical value by time
        self._start = time.time()

#==========================================
# Name: set_end(self)
# Purpose: Gives the self._end variable a new numerical value containing
# the current time in seconds.

# Precondition: Must import time and have the input parameter self,
# or a variable containing a data type StopWatch

# Input Parameter(s): self(Input parameter that allows you to use
# variables containing self. as defined from other functions. May also be
# the variable containing an object of data type StopWatch)

# Return Value(s): Nothing, sets self._end to a new value
#============================================
    def set_end(self): #sets end to a new numerical value by time
        self._end = time.time()

#==========================================
# Name: elapsed_time(self)

# Purpose: Returns the value representing the time that has passed
# by using the difference of self._end and self._start

# Precondition: Must have the input parameter self and also have
# self._end and self._start defined as numerical values with self._end
# being greater than self._start

# Input Parameter(s): elf(Input parameter that allows you to use
# variables containing self. as defined from other functions. May also be
# the variable containing an object of data type StopWatch)

# Return Value(s): A float representing the time that has passed
# by using the difference of self._end and self._start
#============================================
    def elapsed_time(self):
        etime = self._end - self._start
        return float(etime)




#CSCI 1133 Section 19 Lab 006, Problem B, Isaiah Herr

class VideoGame:

#==========================================
# Name: __init__(self, title = '', ESRB = '', ratings = None)
# Purpose: It is the constructor. Defines what variables should
# be passed in for the class and also the defaults in case
# nothing is entered.

# Precondition: Both the title and ESRB must be strings and
# ESRB must be one of the 6 ESRB ratings, E, E10+, T, M, AO, and RP. Ratings must be a list
# and contain only 5 elements at a maximum.

# Input Parameter(s): title (title of the game), ESRB (ESRB rating of the game),
# ratings(a list containing 5 elements that shows the amount of people who
# rated the game and what their review/opinion was from a scale of 1-5)

# Return Value(s): Nothing, sets self variables to equal the input parameters
# for use in other functions
#============================================
    def __init__(self, title = '', ESRB = '', ratings = None): #Our constructor
        if ratings == None:  #Checks to see if ratings isn't defined in the input parameter
            ratings = [0]*5
        self.title = title
        self.ESRB = ESRB
        self.ratings = ratings

#==========================================
# Name: set_title(self, title)

# Purpose: Sets the self.title variable to be equal to the title specified
# in the input parameter when this function is called.

# Precondition: The input parameter, title, must be a string

# Input Parameter(s): self (Important parameter that allows the function to call
# other variables containg self. as specified in the __init__ function.
# title(name of the game that is entered as a input parameter)

# Return Value(s): Nothing, should set self.title to be equal to the title
# specified in the input parameter when this function is called.
#============================================
    def set_title(self, title):
        self.title = title

#==========================================
# Name: set_esrb(self, ESRB)
# Purpose: Sets the self.title variable to be equal to the ESRB rating specified
# in the input parameter when this function is called.

# Precondition: Must be a string and be one of the 6 ESRB ratings which are
# E, E10+, T, M, AO, and RP.

# Input Parameter(s): self (Important parameter that allows the function to call
# other variables containg self. as specified in the __init__ function.
# ESRB(ESRB rating of the game that is entered as an input parameter)

# Return Value(s): Nothing, should set self.title to be equal to the title
# specified in the input parameter when this function is called.
#============================================

    def set_esrb(self, ESRB):
        self.ESRB = ESRB

#==========================================
# Name: get_title(self)

# Purpose: A getter function that returns the value stored within self.title

# Precondition: Must have the input parameter self or the name of
# a variable containing a data type object VideoGame. Returns the
# name of the title of the game.

# Input Parameter(s): self(important input parameter that allows the function to call
# other variables containing self. within the class)

# Return Value(s): Should return the string stored within self.title.
#============================================

    def get_title(self):
        return self.title
#==========================================
# Name: get_esrb(self)

# Purpose: A getter function that returns the value stored within self.title

# Precondition: Must have the input parameter self or the name of
# a variable containing a data type object VideoGame. Must be one of the 6
# ESRB ratings specified

# Input Parameter(s): self(important input parameter that allows the function to call
# other variables containing self. within the class)

# Return Value(s): Returns a string containing the ESRB rating stored within
# self.ESRB
#============================================

    def get_esrb(self):
        return self.ESRB

#==========================================
# Name: get_average(self)

# Purpose: Using the list from ratings, calculates the average score
# rating from users specified in the list.

# Precondition: Must be a list containing 5 elements representing the counts
# of people that have rated the game from 1-5 which is indicated by the index of the list.
# May also contain an empty list or nothing.

# Input Parameter(s): self(allows function to call other variables containing
# self. as specified in the __init__ function)

# Return Value(s): Returns the average of all the ratings as a rounded integer
#============================================

    def get_average(self):
        index = 1 #Indicates the rating of the game from 1-5. Awesome-horrid.
        newlist = [] #Used add values and find the average of the ratings

        if self.ratings == [] or self.ratings == [0]*5: #Checks to see if an empty list is passed in
            self.avgrating = 0 #or a list containing only 0s
        else: #Checks to see if 
            for x in self.ratings: #Adds index to list x amount of times from self.ratings
                newlist.extend([index]*x)
                index = index+1
            self.avgrating = round(sum(newlist)/len(newlist)) #calculates average of newlist
            
#==========================================
# Name: __str__(self)
# Purpose: Tells the class what to print out when asked by the print() function
# Tells the user the name of the title, ESRB rating, and the average rating of
# the video game.

# Precondition: Title and ESRB rating must be a string and the function,
# get_average(self) must be called beforehand in order to print without any
# errors

# Input Parameter(s): self(allows the function to call other variables containing
# self. as specified in the __init__ function and get_average function

# Return Value(s): A string containing the title, ESRB rating, and the average rating
# of the video game
#============================================
    
    def __str__(self): #String that is returned when the data type StopWatch is printed
        return ("Title: " + self.title + ", " + "ESRB Rating: " + self.ESRB + ", "
        + "Average Rating: " + str(self.avgrating))

if __name__ == '__main__':#Used to test if all functions are working within
    import random  #the class
    newlist = []
    newlist2 = []

    print(StopWatch.current_time())
    s1 = StopWatch() #Assigns variable to data type StopWatch
    StopWatch.set_start(s1)
    for x in range(30000): #Indicates the system to use random numbers 30,000 times
        num = random.randint(0, 10000) #Indicates system to use numbers from 0 - 10,000
        newlist.append(num)
    newlist.sort()
    StopWatch.set_end(s1)
    print(StopWatch.elapsed_time(s1)) #Shows the amount of time passed

    print(StopWatch.current_time())
    s1 = StopWatch() #Assigns variable to data type StopWatch
    StopWatch.set_start(s1)
    for x in range(50000):  #Indicates the system to use random numbers 50,000 times
        num = random.randint(0, 10000) #Indicates system to use numbers from 0 - 10,000
        newlist2.append(num)
    newlist.sort()
    StopWatch.set_end(s1)
    print(StopWatch.elapsed_time(s1))
    print(StopWatch.current_time())


    newlst = [] #Used to test if all functions work within class VideoGame
    
    s1 = VideoGame('Hi', 'R', [1,2,3,4,5])
    s2 = VideoGame('There', 'AO', [0,3,2,1,5])
    s3 = VideoGame('There', 'AO')
    newlst.append(s1)
    newlst.append(s2)
    newlst.append(s3)
    print('============') #Separates tests from StopWatch and VideoGame
    for x in newlst: #Finds average of ratings and then prints the string
        x.get_average()   #containing title, ESRB rating, and average ratings
        x.__str__()
        print(x)

    s1.set_title('Hey') #Tests to see if setters and getters are working properly
    s1.set_esrb('AO')
    print(s1.get_esrb())
    print(s1.get_title())
    print(s1)
