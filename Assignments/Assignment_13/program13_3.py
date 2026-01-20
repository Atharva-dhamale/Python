

def ChkPerfect(No):
    
    iSum=0

    for i in range(1,No):
        if(No%i==0):
            iSum+=i

    if No==iSum:
        return True



def main():

    No=int(input("Enter the Number :"))

    Ret=ChkPerfect(No)

    if Ret==True:
        print("Perfect number")
    else:
        print("Not Perfect number")

if __name__=="__main__":
    main()