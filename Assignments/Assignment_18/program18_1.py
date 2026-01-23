
def AddList(No):
    Sum=0
    for num in No:
        Sum=Sum+num

    return Sum

def main():

    No=int(input("Enter the number of elements :"))
    Numbers=[]

    for i in range(1,No+1):
        Value=int(input(f"Enter element {i} :"))
        Numbers.append(Value)

    Ret=AddList(Numbers)

    print("Addition of elements in list are :",Ret)

    


if __name__=="__main__":
    main()