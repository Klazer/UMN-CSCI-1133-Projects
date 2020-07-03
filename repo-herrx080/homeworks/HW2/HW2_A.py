#CSCI 1133 Section 19 Lab 006, Homework Problem A, Isaiah Herr


def poiseuille(L, r, V):
   R = (8*V*L)/(3.14159*r**4)
   return R


def posfun():
    L= float(input("Please enter your length here: "))
    r = float(input("Please enter your radius value here: "))
    V = float(input("Please enter your viscosity value here: "))


    if L > 0 and r > 0 and V > 0:
        print(poiseuille(L, r, V))
    elif L <= 0 or r <= 0 or V <= 0:
        print("Please make sure that all of your inputs are positive. Exiting the program.")
    

posfun()

           
        

    
