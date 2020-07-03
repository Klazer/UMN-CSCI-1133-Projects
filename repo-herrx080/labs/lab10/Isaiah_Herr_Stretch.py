#CSCI 1133 Section 19 Lab 006, Stretch, Isaiah Herr

class Sentence:
    def __init__(self, stri): #Describes how object will be instantiated, constructor
        self.stri = stri

    def __str__(self):
        return str(self.stri)

    def getSentence(self):
        return str(self.stri)
    
    def getWords(self):
        string = self.stri
        words = string.split(" ")
        return words

    def getLength(self):
        character = list(self.stri)
        return len(character)

    def getNumWords(self):
        string = self.stri
        words = string.split(" ")
        return len(words)

    
#CSCI 1133 Section 19 Lab 006, Stretch #2, Isaiah Herr

class SentenceV1:
    def __init__(self, stri):
        self.stri = stri

    def __list__(self):
        string = self.stri
        words = string.split(" ")
        return words
    
    def getSentence(self):
        return str(self.stri)

    def getWords(self):
        string = self.stri
        words = string.split(" ")
        return words

    def getLength(self):
        character = list(self.stri)
        return len(character)

    def getNumWords(self):
        string = self.stri
        words = string.split(" ")
        return len(words)
