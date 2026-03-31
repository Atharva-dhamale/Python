

Addition=lambda A,B: A+B

Subtraction=lambda A,B: A-B


No1=0
No2=0
Ans=0

No1=int(input("Enter first number :"))
No2=int(input("Enter Second number :"))

Ans=Addition(No1,No2)           #Ans=No1+No2        #Lambda function comes here for operation
print("Addition is :",Ans)

Ans=Subtraction(No1,No2)        #Ans=No1-No2        #Lambda function comes here for operation
print("Subtraction is :",Ans)
