
from functools import reduce

Even=lambda No: No%2==0

Square=lambda No: No**2

Sum=lambda No1,No2:No1+No2

def main():

    No=int(input("Enter the no. of elements :"))
    Data=[]

    for i in range(No):
        Number=int(input("Enter the element :"))
        Data.append(Number)

    Ret=list(filter(Even,Data))
    print("Data after filter is :",Ret)

    Ret=list(map(Square,Ret))
    print("Data after map is :",Ret)

    Ret=reduce(Sum,Ret)
    print("Data after reduce is :",Ret)

if __name__=="__main__":
    main()