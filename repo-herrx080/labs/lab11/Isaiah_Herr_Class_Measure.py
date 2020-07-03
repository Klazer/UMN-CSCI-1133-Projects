#CSCI 1133 Section 19 Lab 006, Measure Class, Isaiah Herr

class measure:
    def __init__(self, f=0, i=0):
        while i >= 12: #Adds 1 number to feet continously until i < 12
            i = i-12
            f = f + 1
        if i < 0: #If inches becomes negative, moves down 1 feet and subtracts
            f = f - 1 #The inches left over
            i = 12 + i
        elif f < 0: #If feet is less than 0, everything is 0
            f = 0
            i = 0
        self.f = int(f)
        self.i = int(i)


    def __str__(self):
        if self.i == 0: #Only outputs feet if inches is 0
            return (str(self.f) + "'")
        elif self.f == 0: #Only outputs inches if feet is 0
            return(str(self.i) + '"')
        elif self.i <= 0 and self.f <= 0: #outputs 0 if both i and f is 0
            return('0' + "'")
        else: #returns both feet and inches if both numbers are present
            return (str(self.f) + "'" + str(self.i) + '"')


    def __add__(self, other): #Add overloader
        f = self.f + other.f
        i = self.i + other.i
        return measure(f, i)

    def __sub__(self, other): #Subtract overloader
        f = self.f - other.f
        i = self.i - other.i
        return measure(f, i)
    
            
    
        
