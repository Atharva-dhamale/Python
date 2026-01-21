
Square=lambda No: No**2

def main():
    Data=[2,4,5,6,8,10]

    Ret=list(map(Square,Data))

    print("Data after map is :",Ret)


    

if __name__=="__main__":
    main()