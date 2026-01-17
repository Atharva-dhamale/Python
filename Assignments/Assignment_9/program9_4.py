
def cube(no):
    return no**3

def main():
    Ret=None

    print("Enter Number :")
    no1=int(input())

    Ret=cube(no1)

    print(Ret)

if __name__=="__main__":
    main()