
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

    for point in dataset:
        name, x, y, label = point
        distance = math.sqrt((x_new - x)**2 + (y_new - y)**2)
        distances.append((name, distance, label))

    
    distances.sort(key=lambda x: x[1])

    K = 3
    nearest_neighbors = distances[:K]

    votes = {}
    for neighbor in nearest_neighbors:
        label = neighbor[2]
        if label in votes:
            votes[label] += 1
        else:
            votes[label] = 1

    predicted_class = max(votes, key=votes.get)


    print("\nNearest Neighbors:")
    for neighbor in nearest_neighbors:
        print(f"{neighbor[0]} - Distance: {round(neighbor[1], 2)}")

    print("\nPredicted Class:", predicted_class)



if __name__=="__main__":
    main()