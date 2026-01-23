
def FreqList(No,Search):

    iCount=0

    for num in No:
        if Search==num:
            iCount=iCount+1
        
    return iCount

def main():

    No=int(input("Enter the number of elements :"))
    Numbers=[]

    for i in range(1,No+1):
        Value=int(input(f"Enter element {i} :"))
        Numbers.append(Value)

    Search=int(input("Enter the elements to search :"))

    Ret=FreqList(Numbers,Search)

    print("Frequency of element in list is :",Ret)

    


if __name__=="__main__":
    main()