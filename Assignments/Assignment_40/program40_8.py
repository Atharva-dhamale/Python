
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
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
        max_depth=3,
        random_state=0
    )

    model.fit(X_train, Y_train)
    
    plt.figure(figsize=(20, 10))
    plot_tree(
        model,
        feature_names=feature_cols,
        class_names=["Fail", "Pass"],
        filled=True
    )
    plt.show()
    



if __name__=="__main__":
    main()