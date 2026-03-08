
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def MarvellousClassifier(DataPath):

    border="-"*40

    #Step 1 : Load the dataset from CSV file
    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    df=pd.read_csv(DataPath)

    print(border)
    print("Some entries from dataset")
    print(df.head())
    print(border)

    #Step 2 : Clean the dataset by removing empty rows
    print(border)
    print("Step 2 : Clean the dataset by removing empty rows")
    print(border)

    df.dropna(inplace=True)  #This function deletes the row in which missing value is present
    print("Total Records : ",df.shape[0])
    print("Total Columns : ",df.shape[1])
    print(border)


    X=df.drop(columns=['Class'])
    Y=df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(border)
    print("Input columns : ",X.columns.to_list)
    print("Output columns : Class")

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(border)
    print("Information of training and testing data : ")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    #Step 3 : Train Data
    print(border)
    print("Step 3 : Train Data")
    print(border)

    model=KNeighborsClassifier()
    model.fit(X_train,Y_train)

    #Step 4 : Test Data
    print(border)
    print("Step 4 : Test Data")
    print(border)

    Y_pred=model.predict(X_test)
    


    #Step 5 : Calculate accuracy
    print(border)
    print("Step 5 : Calculate accuracy")
    print(border)

    accuracy=accuracy_score(Y_test,Y_pred)
    print("Accuracy of model is : ",accuracy*100)


    


def main():
    
    border="-"*40

    print(border)
    print("Wine Classifier using KNN")
    print(border)

    MarvellousClassifier("WinePredictor.csv")


if __name__=="__main__":
    main()