
Odd=lambda No: No%2!=0

def main():
    Data=[2,3,4,5,7,10]

    Ret=list(filter(Odd,Data))

    print("Data after filter is :",Ret)


    

if __name__=="__main__":
    main()