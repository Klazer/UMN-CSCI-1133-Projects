#CSCI 1133 Section 19 Lab 006, Warm Up1, Isaiah Herr

import random
def die():

    total = [0,0,0,0,0,0,0,0,0,0,0]
    rolls = 0
    
    while(rolls<10000):

        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        add = die1+die2
        
        if add == 2:
            total[0] = total[0]+1
        elif add == 3:
            total[1] = total[1]+1
        elif add == 4:
            total[2] = total[2]+1
        elif add == 5:
            total[3] = total[3]+1
        elif add == 6:
            total[4] = total[4]+1
        elif add == 7:
            total[5] = total[5]+1
        elif add == 8:
            total[6] = total[6]+1
        elif add == 9:
            total[7] = total[7]+1
        elif add == 10:
            total[8] = total[8]+1
        elif add == 11:
            total[9] = total[9]+1
        elif add == 12:
            total[10] =total[10]+1

        rolls = rolls + 1

    print('2:', total[0])
    print('3:', total[1])
    print('4:', total[2])
    print('5:', total[3])
    print('6:', total[4])
    print('7:', total[5])
    print('8:', total[6])
    print('9:', total[7])
    print('10:', total[8])
    print('11:', total[9])
    print('12:', total[10])


die()
