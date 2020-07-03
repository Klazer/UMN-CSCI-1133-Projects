fileobj = open('somefile','w')
for i in range(3):
    record = '' # start with a null string
    for j in range(1,4):
        record += str(i*3+j) + ','  # append each value and comma
        
    record = record[:-1]  # strip off the last comma, you can also
                            #use record[:5], which does the same thing
                            #For example, if we did record[1:],
                            #We would get a file that shows everything
                            #After position 1, "deleting position 0"
    
    fileobj.write(record) #adds the record changes into the CSV file
    
    if i < 2:
        fileobj.write('\n') # no \n on last record!
        
fileobj.close()
