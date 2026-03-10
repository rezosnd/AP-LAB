import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    "Marks":      [45, 82, 67, 91, 55, 73, 88, 39, 76, 95, 62, 48, 83],
    "Attendance": [80, 95, 70, 98, 60, 85, 92, 50, 88, 99, 75, 65, 90],
    "Assignment": [30, 78, 55, 88, 40, 70, 80, 25, 72, 92, 58, 35, 80],
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

corr_matrix = df.corr()

print("\nCorrelation Matrix:")
print(corr_matrix)

plt.figure(figsize=(7, 5))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.tight_layout()
plt.show()
