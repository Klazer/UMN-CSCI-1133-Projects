#CSCI 1133 Section 9 Lab 006, Homework Problem C, Isaiah Herr

def calories_tall(A, HR, W, T):
    C = int(((A*0.2017)+(HR*0.6309)-(W*0.09036)-55.0969)*T/4.184)
    return C
    

def calories_short(A, HR, W, T):
    C = int(((A*0.074)+(HR*0.4472)-(W*0.05741)-20.4022)*T/4.184)
    return C

def main():
    h = float(input("Please enter your current height as a floating point value (5 feet, 1 inch = 5.1): "))

    A = float(input("Please enter your current age: "))
    HR = float(input("Please enter your average heart rate in bpm during a workout: "))
    W = float(input("Please enter your current weight in pounds: "))
    T = float(input("Please enter the duration of the workout in minutes: "))

    print('=========')
    print("You entered the following info:")
    print("Height:", h)
    print("Age:", A)
    print("Average Heart Rate:", HR)
    print("Weight:", W)
    print("Duration of workout:", T)

    if h <= 5.6 and h > 0:
        calories_short(A, HR, W, T)
        print("The calories burned for this short person is", calories_short(A, HR, W, T), 'calories')
    elif h > 5.6:
        calories_tall(A, HR, W, T)
        print("The calories burned for this tall person is", calories_tall(A, HR, W, T), 'calories')
    elif h <= 0:
        print("That is an impossible number. Please try again with a valid number.")

main()
