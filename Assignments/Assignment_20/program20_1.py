
import threading

def EvenNum():


    for i in range(20):
        if i%2==0:
            print(i,end=" ")
    print("")

def OddNum():
    
    for i in range(20):
        if i%2!=0:
            print(i,end=" ")
    
    print("")

def main():

    Even=threading.Thread(target=EvenNum)
    Odd=threading.Thread(target=OddNum)

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()


if __name__=="__main__":
    main()