
import pandas as pd

def main():

    DatasetPath="student_performance_ml.csv"

    df=pd.read_csv(DatasetPath)
    print("Dataset gets loaded succesfully\n")

    print("Initial entries from dataset\n")
    print(df.head())
    print("\nlast entries from dataset\n")
    print(df.tail())


    print("\nShape of dataset : ",df.shape)
    print("\nColumn names : ",list(df.columns))

    print("\nDatatype of each column : \n")
    print(df.dtypes)


if __name__=="__main__":
    main()