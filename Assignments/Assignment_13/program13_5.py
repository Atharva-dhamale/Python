

def DisplayGrade(No):
    
    if No>=75 and No<=100:
        print("Distinction")
    elif No>=60 and No<75:
        print("First class")
    elif No>=50 and No<60:
        print("Second class")
    elif No<50 and No>=0:
        print("Fail")
    else:
        print("Invalid input")



def main():

    No=int(input("Enter the Number :"))

    DisplayGrade(No)

if __name__=="__main__":
    main()