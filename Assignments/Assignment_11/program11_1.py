

def Prime(No):

    for i in range(2,No):
        if(No%i==0):
            return False
        
    return True
        


def main():

    No=int(input("Enter the number :"))
    Ret=Prime(No)

    if  Ret==True:
        print("It is prime number")
    else:
        print("It is not prime number")

if __name__=="__main__":
    main()