
import numpy as np

image = np.array([
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,1,1,1,1],
    [0,0,0,0,0],
    [0,0,0,0,0]
])

print(image)


kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

print(kernel)


feature_map = np.zeros((3,3))

for i in range(3):
    for j in range(3):
        
        region = image[i:i+3, j:j+3]
      
        result = np.sum(region * kernel)

        feature_map[i][j] = result


print("\nFeature Map (Detected Edge)")
print(feature_map)