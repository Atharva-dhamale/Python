
from sklearn.linear_model import LinearRegression

def Student():

    X=[[1],[2],[3],[4],[5]]

    Y=[50,55,60,65,70]


    model=LinearRegression()

    model.fit(X,Y)

    print("Coefficient for Study hours:", model.coef_[0])

    print("Intercept:", model.intercept_)



def main():

    Student()


if __name__=="__main__":
    main()