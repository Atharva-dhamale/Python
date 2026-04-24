import numpy as np

feature_map = np.array([
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
])

print(feature_map)

relu_output = np.maximum(0, feature_map)
print(relu_output)

def max_pooling(matrix, size=2, stride=1):
    h, w = matrix.shape
    pooled = []
    for i in range(0, h - size + 1, stride):
        row = []
        for j in range(0, w - size + 1, stride):
            window = matrix[i:i+size, j:j+size]
            row.append(np.max(window))
        pooled.append(row)
    return np.array(pooled)

pooled_output = max_pooling(relu_output, 2, 1)
print(pooled_output)