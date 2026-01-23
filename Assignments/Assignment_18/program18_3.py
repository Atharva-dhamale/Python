
def MinList(No):

    Min=No[0]

    for num in No:
        if Min>num:
            Min=num
            


    return Min

def main():

    No=int(input("Enter the number of elements :"))
    Numbers=[]

    for i in range(1,No+1):
        Value=int(input(f"Enter element {i} :"))
        Numbers.append(Value)

    Ret=MinList(Numbers)

    print("Minimum element in list is :",Ret)

    


if __name__=="__main__":
    main()