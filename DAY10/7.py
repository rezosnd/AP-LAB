import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [3, 7, 2, 9, 5, 11, 4, 8, 6, 13]

plt.figure(figsize=(8, 5))
plt.plot(x, y, marker="o", color="blue", linestyle="-", linewidth=2, markersize=7, label="Data Points")

plt.title("Line Graph", fontsize=16)
plt.xlabel("X-axis", fontsize=13)
plt.ylabel("Y-axis", fontsize=13)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
