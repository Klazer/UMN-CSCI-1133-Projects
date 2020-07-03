#Section 1 Lab 006, Warm-Up 1, Isaiah Herr
def pre():
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

#Warm up 2
def CSV():
    import random
    
    name = input('Please enter a name for your file: ')

    file = open(name, 'w')

    for i in range(1000):   #Gives us 1000 lines/records total
        record = ''         #An empty string for each line/record
        
        for field in range(1,3):    #this will give us 2 values for each line
            record += str(random.randint(-1000, 1000)) + ','

        record = record[:-1]    #Removes the last comma

        file.write(record)      #Adds what we have done with record into the file

        if i < 999:
            file.write('\n')    #creates a new line until we reach 1000 lines

    file.close
        
    
    

    


