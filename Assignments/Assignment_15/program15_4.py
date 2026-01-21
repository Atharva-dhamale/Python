
from functools import reduce

Add=lambda No1,No2: No1+No2

def main():
    Data=[2,3,4,5,7,10]

    Ret=reduce(Add,Data)

    print("Data after reduce is :",Ret)


    

if __name__=="__main__":
    main()