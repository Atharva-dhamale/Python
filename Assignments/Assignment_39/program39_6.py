
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():

    DatasetPath="student_performance_ml.csv"

    df=pd.read_csv(DatasetPath)

    feature_cols = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    X = df[feature_cols]
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=1,
        random_state=42
    )

    model.fit(X_train, Y_train)
    
    print("Max_depth=1")

    Training=model.predict(X_train)
    Accuracy=accuracy_score(Y_train,Training)
    print("Training Accuracy : ",Accuracy)


    Testing=model.predict(X_test)
    Accuracy=accuracy_score(Y_test,Testing)
    print("Testing Accuracy : ",Accuracy)


    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,
        random_state=42
    )

    model.fit(X_train, Y_train)
    
    print("Max_depth=3")
    
    Training=model.predict(X_train)
    Accuracy=accuracy_score(Y_train,Training)
    print("Training Accuracy : ",Accuracy)


    Testing=model.predict(X_test)
    Accuracy=accuracy_score(Y_test,Testing)
    print("Testing Accuracy : ",Accuracy)

    model = DecisionTreeClassifier(
        criterion="gini",
        random_state=42
    )

    model.fit(X_train, Y_train)
    
    print("Max_depth=None")
    
    Training=model.predict(X_train)
    Accuracy=accuracy_score(Y_train,Training)
    print("Training Accuracy : ",Accuracy)


    Testing=model.predict(X_test)
    Accuracy=accuracy_score(Y_test,Testing)
    print("Testing Accuracy : ",Accuracy)

    



if __name__=="__main__":
    main()