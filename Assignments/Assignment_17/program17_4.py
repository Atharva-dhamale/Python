
def SumFactors(No):

    Fact=0

    for i in range(1,No):
        if No%i==0:
            Fact+=i
    
    return Fact


def main():

    No=int(input("Enter the number :"))
    Ret=SumFactors(No)
    print("Sum of Factors is :",Ret)


if __name__=="__main__":
    main()