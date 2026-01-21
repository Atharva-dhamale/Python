
from functools import reduce

Divisible=lambda No: No%3==0 and No%5==0

def main():
    Data=[2,5,15,30,33,3,60]

    Ret=list(filter(Divisible,Data))

    print("Data after filter is :",Ret)


    

if __name__=="__main__":
    main()