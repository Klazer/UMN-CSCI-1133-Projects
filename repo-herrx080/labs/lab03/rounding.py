#CSCI 1133 S19 Warm up 2, Isaiah Herr

def roundFloat(x):
    if x > 0:
        y = int(x+0.5)
        return y
    elif x < 0:
        y = int(x-0.5)
        return y
    elif 0 < x < 0.5:
        y = int(x+0.5)
        return y
    elif 0.5<= x < 1:
        y= (int-0.5)
        return y


x = float(input("Please enter a floating point number: "))
print("The rounded number is: ", roundFloat(x))
