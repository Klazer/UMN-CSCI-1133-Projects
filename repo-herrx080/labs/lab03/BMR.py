#CSCI 1133 Lab 3 Warm Up Exercise, Isaiah Herr

print("This will tell you your metabolic weight")

Weight = float(input("Please enter your current weight in pounds: "))
Height = float(input("Please enter your current height in inches: "))
Age = float(input("Please enter your age: "))
Gender = input("Enter M if you are male or F if you are female: ")

BMRF = 655 + (4.3*Weight) + (4.7*Height) - (4.7*Age)
BMRM = 66 + (6.3*Weight) + (12.9*Height) - (6.8*Age)

if Gender == 'M':
    print(" Your metabolic weight is: ", BMRM)

elif Gender == 'F':
    print(" Your metabolic weight is: ", BMRF)

else:
    print("Please type in M or F for your gender and try again")
