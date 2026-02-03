
import os

def main():

    FileName=input("Enter file name :")
    try:
        fobj=open(FileName,"r")

        Ret=os.path.exists(FileName)

        if Ret==True:
            Data=fobj.read()
            print("Data from file is :",Data)
            fobj.close()
            

    except FileNotFoundError:
        print("File not found")

if __name__=="__main__":
    main()