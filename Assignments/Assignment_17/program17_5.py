
def Prime(No):

    for i in range(2,No):
        if No%i==0:
            return False
        
    return True
        
    
    return Fact


def main():

    No=int(input("Enter the number :"))
    Ret=Prime(No)
    
    if Ret==True:
        print("Prime")
    else:
        print("Not Prime")


if __name__=="__main__":
    main()