
def Factorial(No):

    Fact=1

    for i in range(1,No+1):
        Fact*=i
    
    return Fact


def main():

    No=int(input("Enter the number :"))
    Ret=Factorial(No)
    print("Factorial is :",Ret)


if __name__=="__main__":
    main()