#CSCI 1133 Section 19 Lab 006, Warm-Up, Isaiah Herr

class rational:
    def __init__(self,num=0,den=1):
        self.numerator = num
        if den == 0:
            self.denominator = 1
        else:
            self.denominator = den

    def __str__(self):

        if self.denominator == 1:
            return str(self.numerator)
        elif self.numerator == 0:
            return str(0)
        else:
            return str(self.numerator) + '/' + str(self.denominator)


    def scale(self, val):

        self.numerator = self.numerator*val
        self.denominator = self.denominator*val
        
