#CSCI 1133 Section 19 Lab 006, Workout, Isaiah Herr

res = {'False': 0, 'await': 0,'else': 0,'import': 0,'pass': 0,
'None': 0,'break': 0,'except': 0,'in': 0,'raise': 0,
'True': 0,'class': 0,'finally': 0,'is': 0,'return': 0,
'and': 0,'continue': 0, 'for': 0,'lambda': 0,'try': 0,
'as': 0,'def': 0,'from': 0, 'nonlocal': 0,'while': 0,
'assert': 0, 'del': 0,'global': 0,'not': 0,'with': 0,
'async': 0, 'elif': 0, 'if': 0, 'or': 0, 'yield': 0,}

def cnt():
    name = input('Please enter the name of the file: ')

    file = open(name, 'r')

    for x in res:
        for y in file:
            if x not in file:
            res[x] = 0
        else:
            for y in 
            res[x] = count(x)
    return x
