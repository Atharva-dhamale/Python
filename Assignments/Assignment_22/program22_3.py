
class Arithmetic:

    def __init__(self):
        self.Value1=0
        self.Value2=0
        

    def Accept(self):
        self.Value1=int(input("Enter number 1 :"))
        self.Value2=int(input("Enter number 2 :"))



    def Addition(self):
        return self.Value1+self.Value2

    def Subtraction(self):
        return self.Value1-self.Value2

    def Multiplication(self):
        return self.Value1*self.Value2

    def Division(self):
        return self.Value1//self.Value2


def main():

    obj1=Arithmetic()
    obj2=Arithmetic()

    obj1.Accept()
    
    Ret=obj1.Addition()
    print("Addition is :",Ret)

    Ret=obj1.Subtraction()
    print("Subtraction is :",Ret)

    Ret=obj1.Multiplication()
    print("Multiplication is :",Ret)

    Ret=obj1.Division()
    print("Division is :",Ret)


    obj2.Accept()
    
    Ret=obj2.Addition()
    print("Addition is :",Ret)

    Ret=obj2.Subtraction()
    print("Subtraction is :",Ret)

    Ret=obj2.Multiplication()
    print("Multiplication is :",Ret)

    Ret=obj2.Division()
    print("Division is :",Ret)

    

if __name__=="__main__":
    main()