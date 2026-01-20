

AreaRectangle=lambda No1,No2 : No1*No2



def main():

    No1=int(input("Enter Length of rectangle :"))
    No2=int(input("Enter Width of rectangle :"))

    Ret=AreaRectangle(No1,No2)

    print("Area of Rectangle is :",Ret)


if __name__=="__main__":
    main()