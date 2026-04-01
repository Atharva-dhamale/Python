
class Arithmetic:
    def __init__(self,A,B):
        self.No1=A
        self.No2=B
        print("Object gets created succesfully")

    def Addition(self):
        Ans=0
        Ans=self.No1+self.No2
        return Ans
    
    def Subtraction(self):
        Ans=0
        Ans=self.No1-self.No2
        return Ans
    
obj1=Arithmetic(11,10)
obj2=Arithmetic(21,20)

Ret=obj1.Addition()
print(Ret)

Ret=obj2.Subtraction()
print(Ret)