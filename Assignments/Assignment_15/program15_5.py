
from functools import reduce

Max=lambda No1,No2: No1 if No1>No2 else No2

def main():
    Data=[2,3,4,50,7,10]

    Ret=reduce(Max,Data)

    print("Data after reduce is :",Ret)


    

if __name__=="__main__":
    main()