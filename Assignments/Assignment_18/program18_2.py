
def MaxList(No):

    Max=0

    for num in No:
        if Max<num:
            Max=num
            


    return Max

def main():

    No=int(input("Enter the number of elements :"))
    Numbers=[]

    for i in range(1,No+1):
        Value=int(input(f"Enter element {i} :"))
        Numbers.append(Value)

    Ret=MaxList(Numbers)

    print("Maximum element in list is :",Ret)

    


if __name__=="__main__":
    main()