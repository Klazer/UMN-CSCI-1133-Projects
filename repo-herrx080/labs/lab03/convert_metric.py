#CSCI 1333 Section Section 19 Lab 006, Stretch, Isaiah Herr

Answer = 'y'
while Answer == ('y') :
    Value = float(input("Please enter a value: "))
    Unit = input("Please enter a unit: ")
    
    if Unit == 'centimeters':
        inches = Value/2.54
        print(format(inches, "0.4f"), 'inches')
    elif Unit == 'inches':
        centimeters = Value*2.54
        print(format(centimeters, "0.4f"), 'centimeters')
    elif Unit == 'pounds':
        kilos = Value/2.2046
        print(format(kilos, "0.4f"), 'kilos')
    elif Unit == 'kilos':
        pounds = Value*2.2046
        print(format(pounds, "0.4f"), 'pounds')
    elif Unit == 'ounces':
        grams = Value*28.34952
        print(format(grams, "0.4f"), 'grams')
    elif Unit == 'grams':
        ounces = Value/28.34952
        print(format(grams, "0.4f"), 'ounces')
    elif Unit == 'miles':
        kilometers = Value*1.6
        print(format(kilometers, "0.4f"), 'kilometers')
    elif Unit == 'kilometers':
        miles = Value/1.6
        print(format(kilometers, "0.4f"), 'miles')
    else:
        print("That is not a valid unit, please try again")
    
        
    Answer = input('Do you want to continue? (y/n): ')
