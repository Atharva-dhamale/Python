import sys
import DirectoryModule

def WriteLog(message):
    fobj=open("Log1.txt","a")
    fobj.write(message + "\n")


def main():

    try:
        if len(sys.argv) != 4:
            print("Invalid number of argument")

        dirname = sys.argv[1]
        oldext = sys.argv[2]
        newext = sys.argv[3]

        DirectoryModule.ValidateDirectory(dirname)

        Ret = DirectoryModule.RenameFiles(dirname, oldext, newext)

        if len(Ret) == 0:
            WriteLog("No files found to rename.")
        else:
            WriteLog("Renamed files:")
            for files in Ret:
                WriteLog(files)

    except Exception as e:
        WriteLog("Error : " + str(e))


if __name__ == "__main__":
    main()
