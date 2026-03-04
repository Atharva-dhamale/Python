import matplotlib.pyplot as plt

def main():
    
    experience = [1,2,3,4,5]
    salary = [20000,25000,30000,35000,40000]
    
    m = 5000
    c = 15000

    predicted_salary = m*6 + c
    print("Predicted Salary for 6 Years Experience: ₹", predicted_salary)
    
    predicted_line = [m*x + c for x in experience]

    plt.scatter(experience, salary)
    plt.plot(experience, predicted_line)
    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.title("Experience vs Salary")
    plt.show()
    

if __name__=="__main__":
    main()