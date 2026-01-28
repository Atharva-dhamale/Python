
class Demo:
    Value=None

    def __init__(self,A,B):
        self.No1=A
        self.No2=B

    def fun(self):
        print("Inside fun")
        print("Value of No1 :",self.No1)
        print("Value of No2 :",self.No2)

    def gun(self):
        print("Inside gun")
        print("Value of No1 :",self.No1)
        print("Value of No2 :",self.No2)

def main():

    obj1=Demo(11,21)
    obj2=Demo(51,101)

    obj1.fun()
    obj1.gun()
    obj2.fun()
    obj2.gun()
    

if __name__=="__main__":
    main()