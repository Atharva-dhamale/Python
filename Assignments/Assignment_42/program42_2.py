
def main():

    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    n = len(X)


    mean_x = sum(X) / n
    mean_y = sum(Y) / n


    numerator = 0
    denominator = 0

    for i in range(n):
        numerator += (X[i] - mean_x) * (Y[i] - mean_y)
        denominator += (X[i] - mean_x) ** 2

    m = numerator / denominator


    c = mean_y - m * mean_x

    print("Slope (m) =", round(m, 2))
    print("Intercept (c) =", round(c, 2))


    Y_pred = []

    print("\nPredicted Values:")
    for i in range(n):
        y_hat = m * X[i] + c
        Y_pred.append(y_hat)
        print("X =", X[i], "Actual Y =", Y[i], "Predicted Y =", round(y_hat, 2))


    ss_res = 0
    for i in range(n):
        ss_res += (Y[i] - Y_pred[i]) ** 2

    mse = ss_res / n
    print("\nMean Squared Error (MSE) =", round(mse, 2))


    ss_total = 0
    for i in range(n):
        ss_total += (Y[i] - mean_y) ** 2

    r2 = 1 - (ss_res / ss_total)
    print("R² Score =", round(r2, 2))

if __name__=="__main__":
    main()