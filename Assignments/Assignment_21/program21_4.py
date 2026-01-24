
import threading

iSum=0
iProduct=1

def Sum(Arr):

    global iSum

    for i in Arr:
        iSum=iSum+i
    return iSum

def Product(Arr):

    global iProduct

    for i in Arr:
        iProduct=iProduct*i
    return iProduct



def main():

    global iSum
    global iProduct

    Value=int(input("Enter the number of elemnts :"))
    Data=[]

    for i in range(1,Value+1):
        No=int(input(f"Enter the element {i} :"))
        Data.append(No)

    t1=threading.Thread(target=Sum,args=(Data,))
    t2=threading.Thread(target=Product,args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements from list is :",iSum)
    print("Product of elements from list is :",iProduct)

if __name__=="__main__":
    main()