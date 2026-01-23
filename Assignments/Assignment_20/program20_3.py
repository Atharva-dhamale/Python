
import threading

def EvenList(No):

    iSum=0
    iCount=0

    for i in No:
        if i%2==0:
            print(i,end=" ")
            iCount=iCount+1
            iSum=iSum+i
    print("")
    print("Count of even element is :",iCount)
    print("Sum of even number is :",iSum)
    
    

def OddList(No):
    
    iSum=0
    iCount=0

    for i in No:
        if i%2!=0:
            print(i,end=" ")
            iCount=iCount+1
            iSum=iSum+i
    print("")
    print("Count of odd elemnts is :",iCount)
    print("Sum of odd number is :",iSum)
    

def main():

    Data=[93,27,84,31,42,82,25,35,20,10]

    Even=threading.Thread(target=EvenList,args=(Data,))
    Odd=threading.Thread(target=OddList,args=(Data,))

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()




if __name__=="__main__":
    main()