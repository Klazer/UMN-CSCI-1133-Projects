#CSCI 1133, Lab Section 006, Lab 2 Isaiah Herr, Section 2.2

print('This will tell you the current windchill')

t = float(input("Please enter a temperature in degrees: "))
v = float(input("Please enter the wind velocity in miles/hour:"))
windChill = 35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*v**0.16
print("The Windchill Temperature is: ", windChill)
