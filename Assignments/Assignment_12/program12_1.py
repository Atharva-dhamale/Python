

def CheckVowels(Value):

    if Value=='a'or Value=='e' or Value=='i'or Value=='o' or Value=='u':
        return True
    else:
        return False



        


def main():

    Value=input("Enter the number :")
    Ret=CheckVowels(Value)

    if Ret==True:
        print("Vowel")

    else:
        print("Constant")


if __name__=="__main__":
    main()