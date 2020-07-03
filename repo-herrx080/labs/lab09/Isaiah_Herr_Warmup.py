#CSCI 1133 Section 19 Lab 006, Warm-Up, Isaiah Herr

names = ['joe', 'tom', 'barb', 'sue','sally']
scores = [11, 22, 14, 17, 10]
scoredict = {}

def makeDictionary(names, scores):
    pos = 0
    
    for x in names:
        scoredict[x] = scores[pos]
        pos = pos+1

    return scoredict

makeDictionary(names, scores)

def getScore(name, scoredict):

    if name not in scoredict:
        return -1

    else:
        return scoredict[name]


print(getScore(name, scoredict))

