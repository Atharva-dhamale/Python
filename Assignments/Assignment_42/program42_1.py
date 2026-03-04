import math

def main():

        
    
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    n = len(X)

    
    mean_x = sum(X) / n
    mean_y = sum(Y) / n

    print("Mean of X =", mean_x)
    print("Mean of Y =", mean_y)

    
    numerator = 0
    denominator = 0

    for i in range(n):
        numerator += (X[i] - mean_x) * (Y[i] - mean_y)
        denominator += (X[i] - mean_x) ** 2

    m = numerator / denominator

    
    c = mean_y - m * mean_x

    print("Slope (m) =", round(m, 2))
    print("Intercept (c) =", round(c, 2))

    
    print("\nRegression Equation:")
    print("Y =", round(m, 2), "X +", round(c, 2))

    
    x_new = 6
    y_pred = m * x_new + c
    print("\nPredicted Y for X = 6 =", round(y_pred, 2))

if __name__=="__main__":
    main()