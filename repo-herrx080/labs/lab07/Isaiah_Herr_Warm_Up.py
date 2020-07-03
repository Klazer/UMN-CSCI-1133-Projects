#Section 1 Lab 006, Warm-Up, Isaiah Herr

s = " There... are... a... lot ...of: delimiters,,, Ryan?!!!"

for x in ".:,!?":  #for loop is used to remove all characters that contain these
    s = s.replace(x, "") #within the string

s = s.lstrip() #removes the white space from the left
inde = s.find(' Ryan') #Finds the first value that contains the item in the string

s = s.replace(s[inde:], ', Fred') #Replaces the index with the string
s = s.lower() #Makes all letters lowercase
s = s.split(' ') #Makes a list of strings between the white space

print(s)
print(inde)


