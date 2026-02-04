import os

def main():

    FileName = input("Enter file name : ")

    if os.path.exists(FileName):

        fobj = open(FileName, "r")
        
        count = 0
        for line in fobj:
            print(line,end="")

        fobj.close()

        

    else:
        print("File not found")

if __name__ == "__main__":
    main()
