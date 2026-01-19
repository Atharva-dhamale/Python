

def MultTable(No):

    for i in range(1,11):
        Number=No*i
        print(Number)


def main():

    No=int(input("Enter the number :"))
    MultTable(No)

if __name__=="__main__":
    main()