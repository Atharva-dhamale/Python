
import threading

iCnt=0
lobj=threading.Lock()

def Update():

    global iCnt

    for _ in range(100):

        with lobj:

            iCnt=iCnt+1

def main():

    global iCnt
    
    t1=threading.Thread(target=Update)
    t2=threading.Thread(target=Update)
    t3=threading.Thread(target=Update)
    t4=threading.Thread(target=Update)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("Value of iCnt is :",iCnt)



if __name__=="__main__":
    main()