import sys
import DirectoryModule

def WriteLog(message):
    fobj=open("Log.txt","a")
    fobj.write(message + "\n")


def main():

    try:
        if len(sys.argv) != 3:
            print("Invalid number of arguments")
            return

        dirname = sys.argv[1]
        extension = sys.argv[2]

        DirectoryModule.ValidateDirectory(dirname)

        Ret = DirectoryModule.GetFilesByExtension(dirname, extension)

        if len(Ret) == 0:
            WriteLog("No files found with extension " + extension)
        else:
            WriteLog("Files with extension " + extension + " :")
            for file in Ret:
                WriteLog(file)

    except Exception as e:
        WriteLog("Error : " + str(e))


if __name__ == "__main__":
    main()
