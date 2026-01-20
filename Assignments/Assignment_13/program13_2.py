

AreaCircle=lambda No : 3.14*No**2
    


def main():

    No=int(input("Enter radius of circle :"))

    Ret=AreaCircle(No)

    print("Area of Circle is :",Ret)


if __name__=="__main__":
    main()