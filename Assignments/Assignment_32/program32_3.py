import sys
import DirectoryModule

def WriteLog(message):
    fobj=open("Log6.txt","a")
    fobj.write(message + "\n")


def main():

    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: DirectoryDuplicateRemoval.py <dirname>")

        dirname = sys.argv[1]

        DirectoryModule.ValidateDirectory(dirname)

        removed = DirectoryModule.RemoveDuplicates(dirname)

        if len(removed) == 0:
            WriteLog("No duplicate files found to remove.")
        else:
            WriteLog("Removed duplicate files:")
            for f in removed:
                WriteLog(f)

    except Exception as e:
        WriteLog("Error : " + str(e))


if __name__ == "__main__":
    main()
