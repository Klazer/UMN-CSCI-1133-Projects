#CSCI 1133, Lab Section 006, Lab 2 Isaiah Herr, Section 3

Number = float(input("Please enter a four digit number: "))

one = Number//1000

too = Number-one*1000
two = too//100

tree = too-two*100
three = tree//10

four = tree-three*10

print(one)
print(two)
print(three)
print(four)
