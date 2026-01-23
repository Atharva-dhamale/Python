

def Fun(No):
    
    return No%5==0

def main():

    No=int(input("Enter number :"))

    Ret=Fun(No)
    print(Ret)
    

if __name__=="__main__":
    main()