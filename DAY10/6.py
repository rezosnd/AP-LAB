import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"d:\AP LAB\1.csv")

df = df.dropna(subset=["Marks"])

plt.figure(figsize=(12, 6))
plt.bar(df["Name"], df["Marks"], color="steelblue", edgecolor="black")

plt.title("Student Marks", fontsize=16)
plt.xlabel("Student Name", fontsize=13)
plt.ylabel("Marks", fontsize=13)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
