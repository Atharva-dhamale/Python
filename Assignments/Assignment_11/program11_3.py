

def SumDigits(No):

    iSum=0
    iDigit=0

    while(No!=0):
        
        iDigit=No%10
        iSum+=iDigit
        No=No//10
        

    return iSum


        


def main():

    No=int(input("Enter the number :"))
    Ret=SumDigits(No)

    print("Sum of digits are :",Ret)


if __name__=="__main__":
    main()