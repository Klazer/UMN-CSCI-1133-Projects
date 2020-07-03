#CSCI 1133 Section 19 Lab 006, Stretch, Isaiah Herr

import math

mylist = [[45, -99], [24, 83], [-48, -68], [-97, 99], \
[-8, -77], [-2, 50], [44, 41], [-48, -58], \
[-1, 53], [14, 86], [31, 94], [12, -91], \
[33, 50], [82, 72], [83, -90], [10, 78], \
[7, -22], [90, -88], [-21, 5], [6, 23]]


def shortestDist(mylist):

    inf = float("inf")
    
    for i in range(len(mylist)):
        for j in range(i+1, len(mylist)):

            x1 = mylist[i][0]
            y1 = mylist[i][1]
            x2 = mylist[j][0]
            y2 = mylist[j][1]

            dist = math.sqrt((x2 - x1)**2 + (y2-y1)**2)
            if dist < inf:
                inf = dist
    print(inf)

shortestDist(mylist)
