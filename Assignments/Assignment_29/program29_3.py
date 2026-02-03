
import os
import sys

def main():

    if((len(sys.argv)<3) or (len(sys.argv)>3)):
        print("Invalid number of argument")
        return
    
    src=sys.argv[1]
    dest=sys.argv[2]

    if os.path.exists(src)==False:
        print("Source file not found")
        return
    

    
    try:
        fsrc=open(src,"r")
        fdest=open(dest,"w")

        data=fsrc.read()
        fdest.write(data)

        fsrc.close()
        fdest.close()
        
        print("File copied succsefully")
        

    except Exception as e:
        print("Exception :",e)

if __name__=="__main__":
    main()