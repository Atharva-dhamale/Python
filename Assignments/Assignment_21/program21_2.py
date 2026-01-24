
import threading

def Max(Arr):

    Max=0

    for i in Arr:
        if Max<i:
            Max=i
    print("Max element is :",Max)

def Min(Arr):

    Min=Arr[0]

    for i in Arr:
        if Min>i:
            Min=i
    print("Min element is :",Min)



def main():

    Value=int(input("Enter the number of elemnts :"))
    Data=[]

    for i in range(1,Value+1):
        No=int(input(f"Enter the element {i} :"))
        Data.append(No)

    t1=threading.Thread(target=Max,args=(Data,))
    t2=threading.Thread(target=Min,args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()