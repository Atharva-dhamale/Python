import numpy as np

matrix = np.array([
    [6, 4],
    [8, 6]
])

flatten_output = matrix.flatten()
print(flatten_output)

weights = np.array([0.5, 0.2, 0.1, 0.7])
bias = 1

output = np.dot(flatten_output, weights) + bias
print(output)