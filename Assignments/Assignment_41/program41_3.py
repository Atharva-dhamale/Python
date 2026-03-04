import math

def main():

    
    dataset = [
        (2, 60, "Fail"),
        (5, 80, "Pass"),
        (6, 85, "Pass"),
        (1, 50, "Fail")
    ]

    study_hours = float(input("Enter Study Hours: "))
    attendance = float(input("Enter Attendance: "))

    
    distances = []

    for data in dataset:
        hours, attend, result = data
        distance = math.sqrt((study_hours - hours)**2 + (attendance - attend)**2)
        distances.append((distance, result))

    
    distances.sort(key=lambda x: x[0])

    
    K = 3
    nearest_neighbors = distances[:K]

    
    votes = {}

    for neighbor in nearest_neighbors:
        label = neighbor[1]
        votes[label] = votes.get(label, 0) + 1

    predicted_result = max(votes, key=votes.get)

    
    print("\nPredicted Result:", predicted_result)

if __name__=="__main__":
    main()