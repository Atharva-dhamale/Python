import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

def main():
    border="="*40

    print(border)
    print("Step 1 : EDA")
    print(border)
    
    df=pd.read_csv("Bank-full.csv")

    print(df.head())
    print(list(df.columns))
    print(df.isnull().sum())
    print(df.describe())


    print(border)
    print("Step 2 : Data preprocessing")
    print(border)

    X=df.drop("y",axis=1)
    Y=df["y"]

    if Y.dtype == 'object':
        Y = LabelEncoder().fit_transform(Y)

    X = pd.get_dummies(X)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)


    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)


    print(border)
    print("Step 3 : Model Building")
    print(border)

    models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "KNN": KNeighborsClassifier(),
    "Random Forest": RandomForestClassifier()
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
        print("Classification Report:\n", classification_report(Y_test, y_pred))
    

        if hasattr(model, "predict_proba"):
            y_prob = model.predict_proba(X_test)[:, 1]
            roc = roc_auc_score(Y_test, y_prob)
            print("ROC-AUC:", roc)

    print("\nModel Comparison:")
    for k, v in results.items():
        print(k, ":", v)


    best_model_name = max(results, key=results.get)
    best_model = models[best_model_name]

    y_pred = best_model.predict(X_test)
    cm = confusion_matrix(Y_test, y_pred)

    plt.figure()
    sns.heatmap(cm, annot=True, fmt='d')
    plt.title(f"Confusion Matrix - {best_model_name}")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()


    if hasattr(best_model, "predict_proba"):
        y_prob = best_model.predict_proba(X_test)[:, 1]
        fpr, tpr, _ = roc_curve(Y_test, y_prob)

        plt.figure()
        plt.plot(fpr, tpr)
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title(f"ROC Curve - {best_model_name}")
        plt.show()

    

if __name__=="__main__":
    main()















