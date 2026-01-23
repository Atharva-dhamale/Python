
import threading

def Small(Str):

    iCount=0

    for i in Str:
        if i>='a'and i<='z':
            print(i,end=" ")
            iCount=iCount+1
    print("")
    print("Count of Small element is :",iCount,"TID :",threading.get_ident())
    
    

def Capital(Str):

    iCount=0

    for i in Str:
        if i>='A'and i<='Z':
            print(i,end=" ")
            iCount=iCount+1
    print("")
    print("Count of Capital element is :",iCount,"TID :",threading.get_ident())

def Digits(Str):

    iCount=0

    for i in Str:
        if i>='0' and i<='9':
            print(i,end=" ")
            iCount=iCount+1
    print("")
    print("Count of Digits element is :",iCount,"TID :",threading.get_ident())
    

def main():

    String="Atharva13 Kailash93 Dhamale27"

    t1=threading.Thread(target=Small,args=(String,))
    t2=threading.Thread(target=Capital,args=(String,))
    t3=threading.Thread(target=Digits,args=(String,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()




if __name__=="__main__":
    main()