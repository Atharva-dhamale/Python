

def Arithmetic(No1,No2):
    
    Ans1=No1+No2
    Ans2=No1-No2
    Ans3=No1*No2
    Ans4=No1//No2

    return Ans1,Ans2,Ans3,Ans4

def main():

    No1=int(input("Enter the first number :"))
    No2=int(input("Enter the second number :"))
    Ret1,Ret2,Ret3,Ret4=Arithmetic(No1,No2)

    print("Addition is :",Ret1)
    print("Subtraction is :",Ret2)
    print("Multiplication is :",Ret3)
    print("Division is :",Ret4)

    
if __name__=="__main__":
    main()