
import pandas as pd
import matplotlib.pyplot as plt


def main():

    DatasetPath="student_performance_ml.csv"

    df=pd.read_csv(DatasetPath)

    plt.hist(df['StudyHours'])
    plt.ylabel("Study hours")
    plt.xlabel("No. of Students")
    plt.title("Distribution of Study hours")

    plt.show()


if __name__=="__main__":
    main()