

def CheckPalindrome(No):

    temp=No
    iDigit=0
    Rev=0

    while(No!=0):
        
        iDigit=No%10
        Rev = (Rev*10)+iDigit
        No=No//10

    if Rev==temp:
        return True
    else:
        return False



        


def main():

    No=int(input("Enter the number :"))
    Ret=CheckPalindrome(No)

    if Ret==True:
        print("Palindrome")

    else:
        print("Not Palindrome")


if __name__=="__main__":
    main()