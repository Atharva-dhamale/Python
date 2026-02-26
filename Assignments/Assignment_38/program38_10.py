
import pandas as pd
import matplotlib.pyplot as plt


def main():

    DatasetPath="student_performance_ml.csv"

    df=pd.read_csv(DatasetPath)

    passed = df[df['FinalResult'] == 1]
    failed = df[df['FinalResult'] == 0]

    plt.scatter(passed['SleepHours'],passed['FinalResult'],color='green',label='passed')
    plt.scatter(failed['SleepHours'],failed['FinalResult'],color='red',label='failed')
    plt.ylabel("FinalResult")
    plt.xlabel("SleepHours")
    plt.legend()
    plt.title("Scatter plot of SleepHours vs FinalResult")

    plt.show()


if __name__=="__main__":
    main()