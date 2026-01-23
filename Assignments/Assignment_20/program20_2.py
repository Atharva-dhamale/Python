
import threading

def EvenNum(No):

    iSum=0

    for i in range(2,No):
        if No%i==0:
            print(i,end=" ")
            iSum=iSum+i
    print("")
    print("Sum of even factor is :",iSum)
    
    

def OddNum(No):
    
    iSum=0

    for i in range(2,No):
        if No%i!=0:
            print(i,end=" ")
            iSum=iSum+i
    print("")
    print("Sum of odd factor is :",iSum)
    

def main():

    EvenFactor=threading.Thread(target=EvenNum,args=(20,))
    OddFactor=threading.Thread(target=OddNum,args=(20,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main")


if __name__=="__main__":
    main()