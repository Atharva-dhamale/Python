
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

import matplotlib.pyplot as plt

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
        max_depth=5,
        random_state=42
    )

    model.fit(X_train,Y_train)

    print("Model training completed")

    Y_Pred=model.predict(X_test)

    print("Expected answers : ")
    print(list(Y_test))

    print("Predicted answers : ")
    print(Y_Pred)

    accuracy = accuracy_score(Y_test,Y_Pred)
    print("Accuracy of model is : ",accuracy*100)


    cm = confusion_matrix(Y_test,Y_Pred)
    print("Confusion matrix : ")
    print(cm)

    data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)
    data.plot()

    plt.title("Confusion matrix of Student Performance dataset")
    plt.show()



if __name__=="__main__":
    main()