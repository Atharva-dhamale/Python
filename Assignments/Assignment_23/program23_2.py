
class BankAccount:
    ROI=10.5

    def __init__(self):
        self.Name=input("Enter name of Account holder :")
        self.Amount=int(input("Enter Amount balance :"))


    def Display(self):
        print("Name of account holder :",self.Name)
        print("Current Balance :",self.Amount)

    def Deposit(self):
        Value=int(input("Enter amount to deposit :"))
        self.Amount=self.Amount+Value
        print("Current Balance :",self.Amount)

    def Withdraw(self):
        Value=int(input("Enter amount to withdraw :"))

        if Value<self.Amount:
            self.Amount=self.Amount-Value
            print("Current Balance :",self.Amount)
        else:
            print("Please enter valid amount")

    def CalculateInterest(self):
        Interest=(self.Amount*BankAccount.ROI)/100
        print("Interest is :",Interest)



def main():

    obj1=BankAccount()
    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateInterest()

    obj2=BankAccount()
    obj2.Display()
    obj2.Deposit()
    obj2.Withdraw()
    obj2.CalculateInterest()
    

if __name__=="__main__":
    main()