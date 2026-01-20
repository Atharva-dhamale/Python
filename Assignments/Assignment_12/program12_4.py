

def PrintOrder(No):
    
    for i in range(1,No+1):

        print(i,end=" ")
        
    print("")


def main():

    No=int(input("Enter the number :"))
    PrintOrder(No)

    


if __name__=="__main__":
    main()