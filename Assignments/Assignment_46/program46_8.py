from sklearn.linear_model import LinearRegression

def Student():

    X = [[1],[2],[3],[4],[5]]
    Y = [50,55,60,65,70]

    model = LinearRegression()

    model.fit(X,Y)

    pred = model.predict([[6]])

    print("Predicted Marks for 6 study hours:", pred[0])

def main():
    Student()

if __name__=="__main__":
    main()