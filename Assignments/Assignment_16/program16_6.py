

def Fun(No):
    
    if No>0:
        print("Positive Number")

    elif No<0:
        print("Negative Number")

    else:
        print("Zero")

def main():

    No=int(input("Enter number :"))

    Fun(No)
    

if __name__=="__main__":
    main()