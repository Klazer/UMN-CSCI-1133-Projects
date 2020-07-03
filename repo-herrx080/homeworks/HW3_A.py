#CSCI 1133 Section 19 Lab 006, Homework Problem A, Isaiah Herr

def main():
    R = int(input("Please enter a value for red here: "))
    G = int(input("Please enter a value for green here: "))
    B = int(input("Please enter a value for blue here: "))

    print("Red component: ", R)
    print("Green component: ", G)
    print("Blue component: ", B)
    print(RGB_to_CYMK(R, G, B))

        

def RGB_to_CYMK(R, G, B):

    Red = R/255
    Green = G/255
    Blue = B/255

    K = (1 - max(Red,Green,Blue))
    C = ((1-Red - K)/(KK))
    M = ((1-Green-K)/(KK))
    Y = ((1-Blue-K)/(KK))


        
            

    K2 = round(K2*100)
    C2 = round(C2*100)
    M2 = round(M2*100)
    Y2 = round(Y2*100)


    CYMK_list = [C2, M2, Y2, K2]
    CYMK = ' '.join(map(str,CYMK_list))
    return CYMK
    

main()

