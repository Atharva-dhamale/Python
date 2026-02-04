import sys
import DirectoryModule

def WriteLog(message):
    fobj=open("Log4.txt","a")
    fobj.write(message + "\n")


def main():

    try:
        if len(sys.argv) != 2:
            print("Inavlid aruments")

        dirname = sys.argv[1]

        DirectoryModule.ValidateDirectory(dirname)

        checksums = DirectoryModule.GetAllChecksums(dirname)

        if len(checksums) == 0:
            WriteLog("No files found.")
        else:
            WriteLog("File checksums:")
            for fname, chksum in checksums.items():
                WriteLog(f"{fname}  ->  {chksum}")

    except Exception as e:
        WriteLog("Error : " + str(e))


if __name__ == "__main__":
    main()
