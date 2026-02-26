
import pandas as pd

def main():

    DatasetPath="student_performance_ml.csv"

    df=pd.read_csv(DatasetPath)
    
    AvgStudyHour=df['StudyHours'].mean()
    print("Average Study hours is : ",AvgStudyHour)

    AvgAttendance=df['Attendance'].mean()
    print("Average Attendance is : ",AvgAttendance)

    MaxPrevScore=df['PreviousScore'].max()
    print("Maximum previous score is : ",MaxPrevScore)

    MinSleepHour=df['SleepHours'].min()
    print("Minimum Sleep hours is : ",MinSleepHour)


if __name__=="__main__":
    main()