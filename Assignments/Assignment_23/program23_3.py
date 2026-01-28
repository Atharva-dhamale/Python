
class Numbers:

    def __init__(self):
        self.Value=int(input("Enter number :"))


    def ChkPrime(self):
        
        for i in range(2,self.Value):
            if self.Value%i==0:
                return False
        
        return True
    
    def ChkPerfect(self):

        Perfect=0

        for i in range(1,self.Value):
            if self.Value%i==0:
                Perfect=Perfect+i
        if Perfect==self.Value:
            return True
                
        return False
    
    def Factors(self):
        
        print("Factors are :",end="")
        for i in range(2,self.Value):
            if self.Value%i==0:
                print(i,end=" ")
        print("")

    
    def SumFactors(self):
        
        Factor=0

        for i in range(2,self.Value):
            if self.Value%i==0:
                Factor=Factor+i

        return Factor

    


def main():

    obj1=Numbers()

    Ret=obj1.ChkPrime()

    if Ret==True:
        print("Number is Prime")
    else:
        print("Not Prime")

    Ret=obj1.ChkPerfect()

    if Ret==True:
        print("Number is Perfect")
    else:
        print("Not Perfect")

    obj1.Factors()

    Ret=obj1.SumFactors()

    print("Sum of all factors is :",Ret)

    


    obj2=Numbers()

    Ret=obj2.ChkPrime()

    if Ret==True:
        print("Number is Prime")
    else:
        print("Not Prime")

    Ret=obj2.ChkPerfect()

    if Ret==True:
        print("Number is Perfect")
    else:
        print("Not Perfect")

    obj2.Factors()

    Ret=obj2.SumFactors()

    print("Sum of all factors is :",Ret)
    

if __name__=="__main__":
    main()