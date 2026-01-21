
from functools import reduce

Min=lambda No1,No2: No1 if No1<No2 else No2

def main():
    Data=[20,30,4,50,7,10]

    Ret=reduce(Min,Data)

    print("Data after reduce is :",Ret)


    

if __name__=="__main__":
    main()