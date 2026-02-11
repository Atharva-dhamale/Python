
import sys
import psutil
import time


def ProcessDetails(FileName):

    fobj=open(FileName,"w")
    


    for proc in psutil.process_iter(['pid','name']):
        try:
            pid=proc.info['pid']
            name=proc.info['name']
            threads=proc.num_threads()

            fobj.write(f"Process Name : {name}\t\t\t\t,PID : {pid}\t\t\t\t,Threads : {threads}\n")

        except (psutil.NoSuchProcess , psutil.AccessDenied , psutil.ZombieProcess):
            pass

        

    


def main():
    if(len(sys.argv)==2):

        ProcessDetails(sys.argv[1])

    else:
        print("Invalid number of arguments")
        print("1st Argument is executable file name")
        print("2nd Argument is log file name")
        


if __name__=="__main__":
    main()