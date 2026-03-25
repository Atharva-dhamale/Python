import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

def main():
    border="="*40

    print(border)
    print("Step 1 : EDA")
    print(border)
    
    df=pd.read_csv("diabetes.csv")

    print(df.head())
    print(list(df.columns))
    print(df.isnull().sum())
    print(df.describe())


    print(border)
    print("Step 2 : Data preprocessing")
    print(border)

    X=df.drop("Outcome",axis=1)
    Y=df["Outcome"]

    scaler=StandardScaler()
    X_scaled=scaler.fit_transform(X)


    X_train,X_test,Y_train,Y_test=train_test_split(X_scaled,Y,test_size=0.2,random_state=42)


    print(border)
    print("Step 3 : Model Building")
    print(border)

    models = {
    "Decision Tree": DecisionTreeClassifier(),
    "Logistic Regression": LogisticRegression()
    }

    


    print(border)
    print("Step 4 : Model evaluation")
    print(border)


    results = {}

    for name, model in models.items():
        model.fit(X_train, Y_train)
        y_pred = model.predict(X_test)

        acc = accuracy_score(Y_test, y_pred)
        results[name] = acc

        print(f"\n{name}")
        print("Accuracy:", acc)
        print("Confusion Matrix:\n", confusion_matrix(Y_test, y_pred))
        print("Precision:", precision_score(Y_test, y_pred))
        print("Recall:", recall_score(Y_test, y_pred))
        print("F1 Score:", f1_score(Y_test, y_pred))

    
    cm=confusion_matrix(Y_test,y_pred)

    
    plt.figure()
    sns.heatmap(cm,annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()


    print(border)
    print("Step 5 : Final output")
    print(border)

    sample = X_test[0].reshape(1, -1)

    final_model = LogisticRegression()
    final_model.fit(X_train, Y_train)

    prediction = final_model.predict(sample)

    predictions = final_model.predict(X_test)

    output = pd.DataFrame({
        "Actual": Y_test.values,
        "Predicted": predictions
    })

    output.to_csv("predictions.csv", index=False)
    print("Predictions saved to predictions.csv")


    

if __name__=="__main__":
    main()

