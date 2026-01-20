

def Factors(No):
    
    for i in range(1,No+1):
        if(No%i==0):
            print(i,end=" ")
    print("")


def main():

    No=int(input("Enter the number :"))
    Factors(No)

    


if __name__=="__main__":
    main()