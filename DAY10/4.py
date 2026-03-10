import pandas as pd

df = pd.read_csv(r"d:\AP LAB\1.csv")

print("Original DataFrame:")
print(df)

filtered_df = df[df["Marks"] > 60]

print("\nRows where Marks > 60:")
print(filtered_df)
