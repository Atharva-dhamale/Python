
import Arithmetic


def main():

    No1=int(input("Enter first number :"))
    No2=int(input("Enter Second number :"))

    Result=Arithmetic.Add(No1,No2)
    print("Addition is :",Result)

    Result=Arithmetic.Sub(No1,No2)
    print("Subtraction is :",Result)

    Result=Arithmetic.Mult(No1,No2)
    print("Multiplication is :",Result)

    Result=Arithmetic.Div(No1,No2)
    print("Division is :",Result)
    

    


if __name__=="__main__":
    main()