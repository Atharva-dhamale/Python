
def SumDigits(No):

    iDigit=0
    iSum=0
    while(No!=0):
        iDigit=No%10
        iSum=iSum+iDigit
        No=No//10

    return iSum


def main():

    No=int(input("Enter the number :"))
    Ret=SumDigits(No)

    print("Number of digits are :",Ret)


if __name__=="__main__":
    main()