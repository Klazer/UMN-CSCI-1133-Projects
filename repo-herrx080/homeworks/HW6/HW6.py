#CSCI 1133 Section 19 Lab 006, Homework 6, Isaiah Herr

#==========================================
# Name: sameKeys(diction1, diction2)
# Purpose: Creates a new dictionary that adds two values
# to a same key if they are present in both diction 1 and 2
# Precondition: Must consist of either only strings or integers as keys
# Input Parameter(s): diction1 (the first dictionary), diction2 (second one
# with separate lists and values)
# Return Value(s): A new dictionary gets returned with keys that were
# present in both dictionaries along with values that are in a list
#============================================


def sameKeys(diction1, diction2):
    newdict={}
    
    for x in diction1:  #Goes through each key in diction 1
        if x in diction2 :      #If diction 2 also has the same key of x,
            newdict[x]=[diction1[x], diction2[x]] #These values are appended together in the new dictionary

    return newdict

sameKeys(diction1, diction2)

#==========================================
# Name: averageGrades(diction)
# Purpose: Sums and calculates the average of the values for each student/key
# It returns a new dictionary with the sames keys, but with the averages as values
# Precondition: Values must only be integers. Must also not affect the original
# dictionary.
# Input Parameter(s): diction(a dictionary containing students and their
# numerical scores/grades)
# Return Value(s): A new dictionary with the same keys, but with the averages
# of their scores as values. Could also return a 0 if the student
# Has no score or an empty dictionary if there is nothing.
#============================================
def averageGrades(diction):

    newdict = {}
    
    for x in diction:
        if x == []: #Checks to see if the list is empty for a student.
            return 0 # If it is, returns 0
        else: #Finds the average of the student's score
            add = sum(diction[x])
            newdict[x] = int(add/len(x))

    return newdict

averageGrades(diction)
            
    
#==========================================
# Name: allKeys(diction, element)
# Purpose: It takes in a certain value, and checks each key to see
# if it contains that value.
# Precondition: Values and element must always be integers.
# They keys of the dictionaries will always be strings.
# Input Parameter(s): diction(dictionary containing the keys and list of
# integers), element(desired value that we are looking for)
# Return Value(s): Return a list consisting of strings that contained
# the value. Could also return an empty list if none of the keys match
#============================================

def allKeys(diction, element):
    newlist=[]
    
    for key, value in diction.items():
        if element in value: #Checks to see if desired value is in list
            newlist.append(key) #Adds the key to a new list if true
    newlist.sort
    return newlist


allKeys(diction, element)


#==========================================
# Name: invertFiles(files)
# Purpose: Takes all 4 text documents and creates a new dictionary for each
# of them with their respective document numbers. It then creates a new txt
# file containing all of the words sorted in ascending order with their
# document numbers next to them.
# Precondition: Needs all doc1, doc2, doc3, and doc4 txt files.
# Input Parameter(s): files(a list for all 4 of the doc txt files)
# Return Value(s): A new txt file named HW6_output.txt that contains
# all the words used in the 4 doc txt files and their document numbers
# listed next to them.
#============================================

files = ["doc1.txt", "doc2.txt", "doc3.txt", "doc4.txt"]
def invertFiles(files):
    
    newdict = {}
    num = 1
    
    for x in files: #For loop to open up one doc file at a time
        txt = open(x, 'r') 

        for string in txt:
            string = string.lower()
            
            for z in ",;:.?!\n":
                string = string.replace(z, "")
            words = string.split(" ") #Creates a list of all separate words within the txt doc
            words = [word for word in words if not word.isdigit()] #Removes any numbers within strings

            for a in words: #Goes through each word in the list
                if a in newdict and num not in newdict[a]:
                    newdict[a].append(num)
                elif a == '': #Checks to see if an empty string was considered a key
                    pass
                else: #Adds a new key and value to the list if not already in it
                    newdict[a] = [num]

        txt.close

        num = num + 1
    txtfile(newdict)

#==========================================
# Name: txtfile(newdict)
# Purpose: Contains the code that creates the txt file that contains all
# of the words from the 4 doc txt files and along with the numbers listed
# next to the words
# Precondition: It must have newdict, otherwise, it will not work.
# Newdict must be a dictioanry
# Input Parameter(s): newdict(dictionary created using all 4 doc txt files)
# Return Value(s): Shouldn't return anything. Should code for the new
# txt file, HW6_output.txt
#============================================

def txtfile(newdict):
    import csv
    writer = csv.writer(open('HW6_output.txt', 'w')) #Opens up a new doc to write
    for key, value in newdict.items():
        row = writer.writerow([key, value[0]]) #Creates a new row with the key and the value listed next to
        if len(value) > 1: #Checks to see if the key had more than 1 value its list
            row = writer.writerow([key, value[1]])

    writer.close
    
                    
        


