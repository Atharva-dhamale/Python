
from functools import reduce

Length=lambda No: len(No)>5 

def main():
    Data=["Atharva","Jay","Om","Kailash","Dhamale"]

    Ret=list(filter(Length,Data))

    print("Data after filter is :",Ret)


    

if __name__=="__main__":
    main()