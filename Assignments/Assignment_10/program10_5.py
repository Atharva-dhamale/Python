

def Even(No):

    Number=0
    for i in range(1,No+1):
        
        if i%2!=0:
            print(i,end=" ")
    print("")


def main():

    No=int(input("Enter the number :"))
    Even(No)

if __name__=="__main__":
    main()