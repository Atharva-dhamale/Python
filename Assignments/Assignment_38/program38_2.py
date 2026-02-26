
import pandas as pd

def main():

    DatasetPath="student_performance_ml.csv"

    df=pd.read_csv(DatasetPath)
    
    totalStudents=df.shape[0]
    print("Total number of Students is : ",totalStudents)

    passed=(df['FinalResult']==1).sum()
    print("Total passed Students are : ",passed)

    failed=(df['FinalResult']==0).sum()
    print("Total failed Students are : ",failed)





if __name__=="__main__":
    main()