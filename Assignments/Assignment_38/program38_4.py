
import pandas as pd

def main():

    DatasetPath="student_performance_ml.csv"

    df=pd.read_csv(DatasetPath)
    
    ValueCount=df['FinalResult'].value_counts()
    print(ValueCount)

    Percentage=df['FinalResult'].value_counts(normalize=True)*100
    print("Percentage : ",Percentage)



if __name__=="__main__":
    main()