
import os
import sys

def main():

    if((len(sys.argv)<3)or(len(sys.argv)>3)):
        print("Invalid argument")
        return

    f1=sys.argv[1]
    f2=sys.argv[2]
    

    if(os.path.exists(f1)):

        fobj=open(f1,"r")


        for line in fobj:
            if f2 in line.split():
                print(f2," is found")
                return
            
        print(f2,"not found")
            




    else:
        print("File not found")


if __name__ == "__main__":
    main()