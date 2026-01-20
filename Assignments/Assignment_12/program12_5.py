

def PrintReverse(No):
    
    for i in range(No,0,-1):

        print(i,end=" ")
        
    print("")


def main():

    No=int(input("Enter the number :"))
    PrintReverse(No)

    


if __name__=="__main__":
    main()