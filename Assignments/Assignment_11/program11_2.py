

def CountDigits(No):

    iCnt=0

    while(No!=0):
        
        iCnt+=1
        No=No//10
        

    return iCnt


        


def main():

    No=int(input("Enter the number :"))
    Ret=CountDigits(No)

    print("Number of digits in entered number are :",Ret)


if __name__=="__main__":
    main()