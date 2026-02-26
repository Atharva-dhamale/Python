
import pandas as pd
import matplotlib.pyplot as plt


def main():

    DatasetPath="student_performance_ml.csv"

    df=pd.read_csv(DatasetPath)

    plt.boxplot(df['Attendance'])
    plt.title("Attendance Box Plot")

    plt.show()


if __name__=="__main__":
    main()