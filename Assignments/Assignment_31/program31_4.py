import sys
import DirectoryModule

def WriteLog(message):
    fobj=open("Log3.txt","a")
    fobj.write(message + "\n")



def main():

    try:
        if len(sys.argv) != 4:
            print("Invalid arguments")

        src = sys.argv[1]
        dest = sys.argv[2]
        ext=sys.argv[3]

        DirectoryModule.ValidateDirectory(src)

        DirectoryModule.CreateDestinationDirectory(dest)

        files = DirectoryModule.CopyAllFiles(src, dest,ext)

        if len(files) == 0:
            WriteLog("No files found to copy.")
        else:
            WriteLog("Copied files:")
            for f in files:
                WriteLog(f)

    except Exception as e:
        WriteLog("Error : " + str(e))


if __name__ == "__main__":
    main()
