import os

print(os.listdir())
print(os.listdir("News_dataset"))


import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score

# LOAD DATASET
fake = pd.read_csv("News_dataset/Fake.csv")
true = pd.read_csv("News_dataset/True.csv")

# LABELS
fake["label"] = "FAKE"
true["label"] = "REAL"

# COMBINE
data = pd.concat([fake, true])

# INPUT OUTPUT
x = data["text"]
y = data["label"]

# SPLIT
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# VECTORIZATION
vector = TfidfVectorizer(stop_words="english")

xv_train = vector.fit_transform(x_train)
xv_test = vector.transform(x_test)

# MODEL
model = PassiveAggressiveClassifier()

model.fit(xv_train, y_train)

# PREDICT
pred = model.predict(xv_test)

# ACCURACY
acc = accuracy_score(y_test, pred)

print("Accuracy =", acc)

# SAVE
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vector, open("vector.pkl", "wb"))

print("Model Saved Successfully")
