
import sys
import os


def DirectoryScanner(DirName="Marvellous"):
    Ret=False

    Ret=os.path.exists(DirName)
    if(Ret==False):
        print("There is no such directory")
        return
    
    Ret=os.path.isdir(DirName)
    if(Ret==False):
        print("It is not a directory")

    for FolderName,SubFolderName,FileName in os.walk(DirName):
        for fname in FileName:
            fname=os.path.join(FolderName,fname)
            print("File name : ",fname)
            print("File size : ",os.path.getsize(fname))

            if(os.path.getsize(fname)==0):      #Empty
                os.remove(fname)



def main():
    Border="-"*75
    print(Border)
    print("-----------------------Marvellous Directory Automation-------------------")
    print(Border)

    if(len(sys.argv)!=2):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        return
    
    DirectoryScanner(sys.argv[1])


if __name__=="__main__":
    main()