
from functools import reduce

def Prime(No):

    for i in range(2,No):
        if No%i==0:
            return False
    return True

Multiply=lambda No: No*2

Max=lambda No1,No2: No1 if No1>No2 else No2

def main():

    No=int(input("Enter the no. of elements :"))
    Data=[]

    for i in range(No):
        Number=int(input("Enter the element :"))
        Data.append(Number)

    Ret=list(filter(Prime,Data))
    print("Data after filter is :",Ret)

    Ret=list(map(Multiply,Ret))
    print("Data after map is :",Ret)

    Ret=reduce(Max,Ret)
    print("Data after reduce is :",Ret)

if __name__=="__main__":
    main()