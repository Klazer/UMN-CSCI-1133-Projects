#CSCI 1133 Section 19 Lab 006, Homework Problem C, Isaiah Herr


def main():

    P = float(input('Please enter the amount of money you are borrowing: '))
    R = int(input('Please enter the interest rate: '))
    T = int(input('Please enter the the term of the loan in years: '))

    I = (P*(R/100)*T)
    F = P + I
    time = 12
    MP =  F/(time*T)

    print('The face value of the loan is:', '$'+ str(Loan(P,R,T)))
    print('Your monthly payment each month for', time*T, 'months is:', '$'+ str(format(MP, "0.2f")))


def Loan(P,R,T):
    I = (P*(R/100)*T)
    F = P + I
        
    if P < 100 or P > 10000:
        return 'The principal value is too low or too high. The maximum is 10000 and the minimum is 100.'
    elif R <= 0 or R > 15:
        return 'The interest rate is too low or too high. The maximum is 15% and the minimum is 1%.'
    elif T <= 0 or T > 10:
        return 'The term of the loan is too low or too high. The maximum is 10 years and the minimum is 1 year.'
    else:
        return format(F, "0.2f")


main()
        
