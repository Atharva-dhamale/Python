
import math

def main():
    
    dataset = [
        ("A", 1, 2, "Red"),
        ("B", 2, 3, "Red"),
        ("C", 3, 1, "Blue"),
        ("D", 6, 5, "Blue")
    ]

    
    x_new = float(input("Enter X coordinate: "))
    y_new = float(input("Enter Y coordinate: "))


    distances = []
    K=None

    for point in dataset:
        name, x, y, label = point
        distance = math.sqrt((x_new - x)**2 + (y_new - y)**2)
        distances.append((name, distance, label))

    
    distances.sort(key=lambda x: x[1])

   
    nearest_neighbors = distances[:K]

    votes = {}
    for neighbor in nearest_neighbors:
        label = neighbor[2]
        votes[label] = votes.get(label, 0) + 1


    predicted_class = max(votes, key=votes.get)


    print("\nPrediction Results:\n")

    for k in [1, 3, 5]:   
        print("K =", k, "→",predicted_class)




if __name__=="__main__":
    main()