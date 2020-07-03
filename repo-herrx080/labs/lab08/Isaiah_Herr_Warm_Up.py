#Section 19 Lab 006, Warm-Up #1, Isaiah Herr
n = 'olleh'

def reverseString(n):
    if n == '':     #Could also say if len(n) = '' (empty string)
        return ''
    elif len(n) == 1:
        return n

    else:
        return reverseString(n[1:]) + n[0] #This adds the the element at position
                    #0 go at the end of the string at position 1 and the rest
                    #We call the function again and it goes like this:
    #reverseString(lleh) + o --> 'o'
    #reverseString(leh) + l --> 'lo' and so on



#Section 19 Lab 006, Warm-up #2, Isaiah Herr

mylist = [2,87,1,2]

def maxValue(mylist):
    if len(mylist) == 1:
        return mylist[0]

    else:
        ele = mylist[0]
        m = maxValue(mylist[1])

        if ele < mylist[1]:
            mylist.remove(ele)
        elif ele > mylist[1]:
            mylist.remove(mylist[1])
        

print(maxValue(mylist))
