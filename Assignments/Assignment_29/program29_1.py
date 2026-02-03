
import os

def main():

    FileName=input("Enter file name :")

    Ret=os.path.exists(FileName)

    if Ret==True:
        print("File exists")
    else:
        print("File not found")

if __name__=="__main__":
    main()