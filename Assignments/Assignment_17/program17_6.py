
def Pattern(No):


    for i in range(No,0,-1):
        print("*"*i)
    print("")


def main():

    No=int(input("Enter the number :"))
    Pattern(No)


if __name__=="__main__":
    main()

