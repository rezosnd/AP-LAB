import pandas as pd

df = pd.read_csv(r"d:\AP LAB\1.csv")

print("Head (first 5 rows):")
print(df.head())

print("\nTail (last 5 rows):")
print(df.tail())

print("\nDescribe (summary statistics):")
print(df.describe())
