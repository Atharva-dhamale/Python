

def ReverseDigits(No):

    
    iDigit=0

    while(No!=0):
        
        iDigit=No%10
        print(iDigit,end="")
        No=No//10

    print("")


        


def main():

    No=int(input("Enter the number :"))
    ReverseDigits(No)



if __name__=="__main__":
    main()