import sys
import DirectoryModule

def WriteLog(message):
    fobj=open("Log5.txt","a")
    fobj.write(message + "\n")


def main():

    try:
        if len(sys.argv) != 2:
            print("Inavlid aruments")

        dirname = sys.argv[1]

        DirectoryModule.ValidateDirectory(dirname)

        dupfiles = DirectoryModule.FindDuplicates(dirname)

        if len(dupfiles) == 0:
            WriteLog("No duplicate files found.")
        else:
            WriteLog("Duplicate files:")
            for f in dupfiles:
                WriteLog(f)

    except Exception as e:
        WriteLog("Error : " + str(e))


if __name__ == "__main__":
    main()
