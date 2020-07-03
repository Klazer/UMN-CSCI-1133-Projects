#CSCI 1133 Section 19 Lab 006, Vector, Isaiah Herr
import math

class vector:
    def __init__(self, vector = [0, 0, 0]):
        self.vector = vector

    def __str__(self):
        return self.vector

    def getValues(self):
        return self.vector

    def setValues(self, other):
        self.vector = other

    def magnitude(self):
        for x in self.vector:
            x = x**2
        self.vector = sum(self.vector)
        self.vector = float(math.sqrt(self.vector))
        return self.vector
        
    def __add__(self, other):
        while len(self.vector) < len(other.vector):
            pop(other.vector)
        
        

    def __mul__(self, other):

        
            
