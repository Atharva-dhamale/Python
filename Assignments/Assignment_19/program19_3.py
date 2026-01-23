
from functools import reduce

fun=lambda No: No>=70 and No<=90

gun=lambda No: No+10

sun=lambda No1,No2:No1*No2

def main():

    No=int(input("Enter the no. of elements :"))
    Data=[]

    for i in range(No):
        Number=int(input("Enter the element :"))
        Data.append(Number)

    Ret=list(filter(fun,Data))
    print("Data after filter is :",Ret)

    Ret=list(map(gun,Ret))
    print("Data after map is :",Ret)

    Ret=reduce(sun,Ret)
    print("Data after reduce is :",Ret)

if __name__=="__main__":
    main()