import os

def main():

    FileName = input("Enter file name : ")

    if os.path.exists(FileName):

        fobj = open(FileName, "r")

        wordCount = 0
        for line in fobj:
            words=line.split()
            wordCount=wordCount+len(words)

        fobj.close()

        print("File exists")
        print("Total number of words :", wordCount)

    else:
        print("File not found")

if __name__ == "__main__":
    main()
