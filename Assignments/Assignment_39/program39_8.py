import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)


def main():

    Border = "-"*40

    #########################################################
    # Step 1 : Load the dataset
    #########################################################

    print(Border)
    print("Step 1 : Load the dataset")
    print(Border)

    DatasetPath = "student_performance_ml.csv"

    df = pd.read_csv(DatasetPath)

    print("Dataset gets loaded succesfully...")


    #########################################################
    # Step 2 : Data Analysis (EDA)
    #########################################################

    print(Border)
    print("Step 2 : Data analysis")
    print(Border)

    print("Shape of dataset : ",df.shape)
    print("Column Names : ",list(df.columns))

    print("Missing values (Per Column)")
    print(df.isnull().sum())

    print("Class Distribution (Result count)")
    print(df["FinalResult"].value_counts())

    print("Statistical Report of dataset")
    print(df.describe())

    #########################################################
    # Step 3 : Decide Independent & Dependent variables
    #########################################################

    print(Border)
    print("Step 3 : Decide Independent & Dependent variables")
    print(Border)

    # X : Independent variables / Fetures
    # Y : Dependent variables / Labels

    feature_cols = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    X = df[feature_cols]
    Y = df["FinalResult"]

    print("X shape : ",X.shape)
    print("Y shape : ",Y.shape)

    #########################################################
    # Step 4 : Visualisation of dataset
    #########################################################

    print(Border)
    print("Step 4 : Visualisation of dataset")
    print(Border)

    # Scatter plot
    plt.figure(figsize=(7,5))

    for res in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == res]
        plt.scatter(temp["AssignmentsCompleted"], temp["PreviousScore"], label = res)

    plt.title("Student Performance : AssignmentsCompleted vs PreviousScore")

    plt.xlabel("AssignmentsCompleted")
    plt.ylabel("PreviousScore")

    plt.legend()
    plt.grid(True)
    plt.show()

    #########################################################
    # Step 5 : Split the dataset for training and testing
    #########################################################

    print(Border)
    print("Step 5 : Split the dataset for training and testing")
    print(Border)

    

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.3,
        random_state=42
    )

    print("Data splitting activity done : ")


    #########################################################
    # Step 6 : Build the model
    #########################################################

    print(Border)
    print("Step 6 : Build the model")
    print(Border)

    print("We are going to use DecisionTreeClassifier")

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,
        random_state=42
    )

    print("Model succesfully created : ",model)

    #########################################################
    # Step 7 : Train the model
    #########################################################

    print(Border)
    print("Step 7 : Train the model")
    print(Border)

    model.fit(X_train,Y_train)

    print("Model training completed")

    #########################################################
    # Step 8 : Evaluate the model
    #########################################################

    print(Border)
    print("Step 8 : Evaluate the model")
    print(Border)

    Y_pred = model.predict(X_test)

    print("Model evaluation (testing) complete")

    print(Y_pred.shape)

    print("Expected answers : ")
    print(list(Y_test))

    print("Predicted answers : ")
    print(list(Y_pred))

    #########################################################
    # Step 9 : Evaluate the model performance
    #########################################################

    print(Border)
    print("Step 9 : Evaluate the model performance")
    print(Border)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of model is : ",accuracy*100)

    cm = confusion_matrix(Y_test,Y_pred)
    print("Confusion matrix : ")
    print(cm)

    print("Classification Report")
    print(classification_report(Y_test,Y_pred))

    #########################################################
    # Step 10 : Plot confusion matrix
    #########################################################

    print(Border)
    print("Step 10 : Plot confusion matrix")
    print(Border)

    data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)
    data.plot()

    plt.title("Confusion matrix of Iris dataset")
    plt.show()


if __name__=="__main__":
    main()