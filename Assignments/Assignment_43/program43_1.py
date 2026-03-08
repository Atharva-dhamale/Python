import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

DatasetPath = "PlayPredictor.csv"

df = pd.read_csv(DatasetPath)

df["Whether"] = df["Whether"].map({"Sunny":0,"Overcast":1,"Rain":2})
df["Temperature"] = df["Temperature"].map({"Hot":0,"Mild":1,"Cool":2})

df=df.dropna()

feture_cols = [
    "Whether",
    "Temperature"
]

X = df[feture_cols]
Y = df["Play"]

model=KNeighborsClassifier(n_neighbors=3)

model.fit(X,Y)

Y_pred = model.predict(X)
accuracy = accuracy_score(Y, Y_pred)

print("Accuracy :", accuracy*100)

new_point=np.array([[0,0]])


Prediction = model.predict(new_point)

print("Predicted Label : ",Prediction[0])

