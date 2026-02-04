import os

def main():

    FileName = input("Enter file name : ")

    if os.path.exists(FileName):

        fobj = open(FileName, "r")

        count = 0
        for line in fobj:
            count = count + 1

        fobj.close()

        print("File exists")
        print("Total number of lines :", count)

    else:
        print("File not found")

if __name__ == "__main__":
    main()
