
import pandas as pd
import matplotlib.pyplot as plt


def main():

    DatasetPath="student_performance_ml.csv"

    df=pd.read_csv(DatasetPath)

    passed = df[df['FinalResult'] == 1]
    failed = df[df['FinalResult'] == 0]

    plt.scatter(passed['StudyHours'],passed['PreviousScore'],color='green',label='passed')
    plt.scatter(failed['StudyHours'],failed['PreviousScore'],color='red',label='failed')
    plt.ylabel("Previous Score")
    plt.xlabel("Study Hour")
    plt.legend()
    plt.title("Scatter plot of StudyHours vs PreviousScore")

    plt.show()


if __name__=="__main__":
    main()