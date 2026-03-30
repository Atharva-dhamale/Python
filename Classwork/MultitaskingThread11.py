
import threading
import time


def SumOdd(No):
    
    sum=0

    for i in range(1,No+1,2):
        sum=sum+i

    print("Odd Sum is :",sum)
    
    

def main():
    
    start_time=time.time()
    SumOdd(100000000)
    end_time=time.time()

    print("Time reaquired :",end_time-start_time)


if __name__=="__main__":
    main()