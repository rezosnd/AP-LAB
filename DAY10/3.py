import pandas as pd

df = pd.read_csv(r"d:\AP LAB\1.csv")

print("Before replacing missing values:")
print(df)
print("\nMissing values per column:")
print(df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nAfter replacing missing values with mean:")
print(df)
