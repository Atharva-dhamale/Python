from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import euclidean
import numpy as np

data = np.array([[25,20000],[30,40000]])


dist_before = euclidean(data[0], data[1])

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

dist_after = euclidean(scaled_data[0], scaled_data[1])

print("Distance before scaling:", dist_before)
print("Distance after scaling:", dist_after)