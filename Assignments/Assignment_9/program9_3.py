
def square(no):
    return no**2

def main():
    Ret=None

    print("Enter Number :")
    no1=int(input())

    Ret=square(no1)

    print(Ret)

if __name__=="__main__":
    main()