
def divisible(no):
    if no%3==0 and no%5==0:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

def main():

    print("Enter Number :")
    no1=int(input())

    divisible(no1)

if __name__=="__main__":
    main()