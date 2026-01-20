

def Binary(No):
    
    binary = ""

    if No == 0:
        binary = "0"
    else:
        while No> 0:
            binary = str(No % 2) + binary
            No = No // 2

    return binary



def main():

    No=int(input("Enter the Number :"))

    Ret=Binary(No)

    print("Binary equivalent is :",Ret)

if __name__=="__main__":
    main()