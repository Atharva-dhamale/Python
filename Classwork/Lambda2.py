
#Functional Approach(lambda)

CheckEven=lambda No:(No%2==0)

def main():
    Value=0
    Ret=False
    print("Enter number :")
    Value=int(input())

    Ret=CheckEven(Value)

    if(Ret==True):
        print("It is even")

    else:
        print("It is odd")



if __name__=="__main__":
    main()