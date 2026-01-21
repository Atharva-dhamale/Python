
from functools import reduce

Product=lambda No1,No2: No1*No2

def main():
    Data=[2,4,6,8,10]

    Ret=reduce(Product,Data)

    print("Data after reduce is :",Ret)


    

if __name__=="__main__":
    main()