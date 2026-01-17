
def ChkGreater(no1,no2):
    if(no1>no2):
        print(no1,"is greater")
    else:
        print(no2,"is greater")

def main():
    print("Number 1:")
    no1=int(input())
    print("Number 2:")
    no2=int(input())
    ChkGreater(no1,no2)

if __name__=="__main__":
    main()