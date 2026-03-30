
import threading


def SumOdd(No):
    
    sum=0

    for i in range(1,No+1,2):
        sum=sum+i

    print("Odd Sum is :",sum)
    
    

def main():
    
    SumOdd(100000000)



if __name__=="__main__":
    main()