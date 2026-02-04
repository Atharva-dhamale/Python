
import os
import sys

def main():

    if((len(sys.argv)<3) or(len(sys.argv)>3)):
        print("Inavlid arguments")
        return
    
    f1=sys.argv[1]
    f2=sys.argv[2]

    try:

        src=open(f1,"r")
        dest=open(f2,"w")

        fobj=src.read()
        dest.write(fobj)

        src.close()
        dest.close()

        print("Contents of a.txt copied into b.txt")

    except FileNotFoundError as e:
        print("Exception :",e)



if __name__ == "__main__":
    main()