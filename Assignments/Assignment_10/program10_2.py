

def Sum(No):

    Number=0
    for i in range(1,No+1):
        Number=Number+i

    print(Number)


def main():

    No=int(input("Enter the number :"))
    Sum(No)

if __name__=="__main__":
    main()