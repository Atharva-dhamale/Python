
import os
import sys

def main():

    if((len(sys.argv)<3) or (len(sys.argv)>3)):
        print("Invalid number of argument")
        return
    
    f1=sys.argv[1]
    f2=sys.argv[2]

    
    

    
    try:
        file1=open(f1,"r")
        file2=open(f2,"r")

        data1=file1.read()
        data2=file2.read()

        if data1==data2:
            print("Success")
        else:
            print("Failure")
        

    except Exception as e:
        print("Exception :",e)

if __name__=="__main__":
    main()