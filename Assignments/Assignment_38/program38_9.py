
import pandas as pd
import matplotlib.pyplot as plt


def main():

    DatasetPath="student_performance_ml.csv"

    df=pd.read_csv(DatasetPath)

    plt.scatter(df['AssignmentsCompleted'],df['FinalResult'])
    plt.ylabel("FinalResult")
    plt.xlabel("AssignmentsCompleted")
    plt.title("Relationship between AssignmentCompleted and FinalResult")

    plt.show()


if __name__=="__main__":
    main()