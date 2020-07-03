#CSCI 1133, Lab Section 006, Lab 2 Isaiah Herr, Section 2.3

print('This program will tell you what your monthly loan payment will be')

loan_amount = float(input("Please enter the amount you plan to loan: "))
r = float(input("Please enter the annual interest rate: "))
n = float(input("Please enter the loan duration in months: "))
Payment = r*(loan_amount)/1-(1+r)**-n

print("Your monthly payments will be: ", Payment, "$")
