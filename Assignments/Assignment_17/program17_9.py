
def Digits(No):

    iDigit=0
    iCount=0
    while(No!=0):
        iDigit=No%10
        iCount=iCount+1
        No=No//10

    return iCount


def main():

    No=int(input("Enter the number :"))
    Ret=Digits(No)

    print("Number of digits are :",Ret)


if __name__=="__main__":
    main()