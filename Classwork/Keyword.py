

def EmployeeInfo(Name,Age,Salary,City):
    print("Name :",Name)
    print("Age :",Age)
    print("Salary :",Salary)
    print("City :",City)
    

def main():
    #Positional

    #EmployeeInfo("Atharva",21,2000.50,"Pune")           #Correct
    #EmployeeInfo(26,"Atharva","Pune",2000.50)           #Wrong

    #Keyword
    EmployeeInfo(Age=21,Name="Atharva",City="Pune",Salary="2000.50")        #Correct

if __name__=="__main__":
    main()