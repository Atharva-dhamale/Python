
import MarvellousNum


def main():

    No=int(input("Enter the number of elements :"))
    Numbers=[]

    for i in range(1,No+1):
        Value=int(input(f"Enter element {i} :"))
        Numbers.append(Value)

    Ret=MarvellousNum.ListPrime(Numbers)
    print("Sum of Prime number is :",Ret)

    


if __name__=="__main__":
    main()