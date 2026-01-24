
import threading

def isPrime(num):

    for i in range(2,num):
        if num%i==0:
            return False
    return True

def Prime(No):

    print("Prime numbers are :")
    for i in No:
        if isPrime(i):
            print(i,end=" ")
    print("")

def NonPrime(No):

    print("Non Prime numbers are :")
    for i in No:
        if not isPrime(i):
            print(i,end=" ")
    print("")



def main():

    Data=[93,27,84,31,25,35,48,13,43,7]

    t1=threading.Thread(target=Prime,args=(Data,))
    t2=threading.Thread(target=NonPrime,args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()