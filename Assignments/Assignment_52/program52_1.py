import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def main():

    try:
        df = pd.read_csv('student-mat.csv', sep=';')
    except FileNotFoundError:
        print("Error: Please ensure 'student-mat.csv' is in the working directory.")
        
        data = {
            'G1': [18, 5, 12, 15, 6], 'G2': [17, 6, 11, 14, 5], 'G3': [19, 4, 10, 16, 2],
            'studytime': [4, 1, 2, 3, 1], 'failures': [0, 3, 1, 0, 2], 'absences': [2, 15, 6, 4, 20]
        }
        df = pd.DataFrame(data)


    features = ['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']
    x = df[features]


    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)


    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(x_scaled)


    cluster_means = df.groupby('Cluster')['G3'].mean().sort_values(ascending=False)
    mapping = {
        cluster_means.index[0]: "Top Performers (Cluster 0)",
        cluster_means.index[1]: "Average Students (Cluster 1)",
        cluster_means.index[2]: "Struggling Students (Cluster 2)"
    }

    df['Cluster_Name'] = df['Cluster'].map(mapping)

    print("--- Cluster Summary (Mean Values) ---")
    print(df.groupby('Cluster_Name')[features].mean())

    print("\n--- Sample Output ---")
    print(df[['G3', 'studytime', 'failures', 'absences', 'Cluster_Name']].head(10))

if __name__=="__main__":
    main()