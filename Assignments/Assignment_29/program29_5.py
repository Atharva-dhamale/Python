
import os
import sys

def main():

    if((len(sys.argv)<3) or (len(sys.argv)>3)):
        print("Invalid number of argument")
        return
    
    f1=sys.argv[1]
    string=sys.argv[2]

    if os.path.exists(f1)==False:
        print("file not found")
        return

    
    

    
    try:
        file1=open(f1,"r")

        data1=file1.read()

        count=data1.count(string)

        print("String found ",count,"times")

        file1.close()

        

    except Exception as e:
        print("Exception :",e)

if __name__=="__main__":
    main()