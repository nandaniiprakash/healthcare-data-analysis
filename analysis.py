import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("heart.csv")

# basic info
print(df.head())
print(df.describe())

# check missing values
print(df.isnull().sum())

# simple analysis
print("Average age:", df["age"].mean())

# plot age distribution
df["age"].hist()
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
