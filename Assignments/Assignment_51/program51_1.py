import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def main():
    
    # ==========================================
    # Part 1: Data Preprocessing
    # ==========================================

    try:
        fake_df = pd.read_csv('Fake.csv')
        true_df = pd.read_csv('True.csv')
        
        fake_df['label'] = 0
        true_df['label'] = 1

        
        df = pd.concat([fake_df, true_df], axis=0).sample(frac=1).reset_index(drop=True)
    except FileNotFoundError:
        print("Error: Ensure both 'Fake.csv' and 'True.csv' are available.")
        exit()


    df['content'] = df['title'] + " " + df['text']
    df = df.dropna(subset=['content'])

    X = df['content']
    y = df['label']


    X_train_raw, X_test_raw, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # ==========================================
    # Part 2: Feature Extraction
    # ==========================================


    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    X_train = tfidf.fit_transform(X_train_raw)
    X_test = tfidf.transform(X_test_raw)

    # ==========================================
    # Part 3: Model Training
    # ==========================================


    lr_model = LogisticRegression(solver='liblinear')
    dt_model = DecisionTreeClassifier(max_depth=10, random_state=42)


    hard_voting = VotingClassifier(
        estimators=[('lr', lr_model), ('dt', dt_model)],
        voting='hard'
    )


    soft_voting = VotingClassifier(
        estimators=[('lr', lr_model), ('dt', dt_model)],
        voting='soft'
    )


    models = {
        "Logistic Regression": lr_model,
        "Decision Tree": dt_model,
        "Hard Voting": hard_voting,
        "Soft Voting": soft_voting
    }

    # ==========================================
    # Part 4: Evaluation
    # ==========================================

    print("--- Model Performance Comparison ---")
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print(f"{name} Accuracy: {accuracy_score(y_test, y_pred):.4f}")


    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()

    for i, (name, model) in enumerate(models.items()):
        y_pred = model.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[i])
        axes[i].set_title(f'Confusion Matrix: {name}')
        axes[i].set_xlabel('Predicted')
        axes[i].set_ylabel('Actual')

    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    main()