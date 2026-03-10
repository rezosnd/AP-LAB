import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
# 1. Read monthly sales data from CSV
df = pd.read_csv(r"d:\AP LAB\DAY10\sales_data.csv")
print("=" * 55)
print("SALES DATA ANALYSIS")
print("=" * 55)
print("\n[1] First 5 rows of dataset:")
print(df.head())
# 2. Total and Average Sales
total_sales = df["Revenue"].sum()
avg_sales   = df["Revenue"].mean()
print("\n[2] Sales Summary:")
print(f"    Total Sales  : {total_sales:,.2f}")
print(f"    Average Sales: {avg_sales:,.2f}")
# 3. Highest and Lowest Sales Month
monthly_sales = df.groupby("Month")["Revenue"].sum()
highest_month = monthly_sales.idxmax()
lowest_month  = monthly_sales.idxmin()
print("\n[3] Monthly Sales:")
print(monthly_sales.sort_values(ascending=False).to_string())
print(f"\n    Highest Sales Month: {highest_month} -> {monthly_sales[highest_month]:,.2f}")
print(f"    Lowest  Sales Month: {lowest_month}  -> {monthly_sales[lowest_month]:,.2f}")

# 4. Filter Sales Greater Than Threshold
threshold    = 1000
filtered_df  = df[df["Revenue"] > threshold]
print(f"\n[4] Records with Revenue > {threshold}: {len(filtered_df)} / {len(df)}")
print(filtered_df[["Date", "Month", "Product", "Revenue"]].head(5).to_string(index=False))

# 5. NumPy Array & Statistics
sales_array = np.array(df["Revenue"])
print("\n[5] NumPy Sales Statistics:")
print(f"    Sum      : {np.sum(sales_array):,.2f}")
print(f"    Mean     : {np.mean(sales_array):,.2f}")
print(f"    Median   : {np.median(sales_array):,.2f}")
print(f"    Std Dev  : {np.std(sales_array):,.2f}")
print(f"    Min      : {np.min(sales_array):,.2f}")
print(f"    Max      : {np.max(sales_array):,.2f}")
print(f"    25th %ile: {np.percentile(sales_array, 25):,.2f}")
print(f"    75th %ile: {np.percentile(sales_array, 75):,.2f}")

# 6. Bar Chart – Product Sales Comparison
product_sales = df.groupby("Product_Category")["Revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
plt.bar(product_sales.index, product_sales.values,
        color=["steelblue", "coral", "mediumseagreen"], edgecolor="black")
plt.title("Product Sales Comparison", fontsize=16)
plt.xlabel("Product Category", fontsize=13)
plt.ylabel("Total Revenue", fontsize=13)
plt.tight_layout()
plt.savefig(r"d:\AP LAB\DAY10\bar_chart.png")
print("[6] Bar chart saved as bar_chart.png")
plt.close()

# 7. Line Graph – Monthly Sales Trend
month_order = ["January","February","March","April","May","June",
               "July","August","September","October","November","December"]
monthly_sales_ordered = monthly_sales.reindex([m for m in month_order if m in monthly_sales.index])

plt.figure(figsize=(12, 5))
plt.plot(monthly_sales_ordered.index, monthly_sales_ordered.values,
         marker="o", color="royalblue", linewidth=2, markersize=7, label="Monthly Revenue")
plt.title("Monthly Sales Trend", fontsize=16)
plt.xlabel("Month", fontsize=13)
plt.ylabel("Total Revenue", fontsize=13)
plt.xticks(rotation=45, ha="right")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(r"d:\AP LAB\DAY10\line_graph.png")
print("[7] Line graph saved as line_graph.png")
plt.close()
# 8. Correlation – Advertising Cost vs Sales
corr_matrix = df[["Cost", "Revenue", "Profit"]].corr()
corr_value  = df["Cost"].corr(df["Revenue"])
print("\n[8] Correlation Matrix (Cost, Revenue, Profit):")
print(corr_matrix)
print(f"\n    Correlation between Cost and Revenue: {corr_value:.4f}")

plt.figure(figsize=(7, 5))
plt.scatter(df["Cost"], df["Revenue"], alpha=0.4, color="darkorange", edgecolors="black")
plt.title(f"Cost vs Revenue  (r = {corr_value:.2f})", fontsize=14)
plt.xlabel("Cost", fontsize=12)
plt.ylabel("Revenue", fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.savefig(r"d:\AP LAB\DAY10\correlation.png")
print("[8] Scatter plot saved as correlation.png")
plt.close()
# 9. Matrix Multiplication – Sales Forecasting
df["Quarter"] = pd.to_datetime(df["Date"]).dt.quarter
pivot = df.pivot_table(values="Revenue", index="Product_Category",
                       columns="Quarter", aggfunc="sum", fill_value=0)
sales_matrix = pivot.values.astype(float)
n = sales_matrix.shape[1]

forecast_weights = np.array([[1.05, 0.02, 0.01, 0.00],
                              [0.03, 1.08, 0.02, 0.00],
                              [0.01, 0.03, 1.10, 0.00],
                              [0.00, 0.00, 0.00, 1.06]])[:n, :n]

forecasted = np.dot(sales_matrix, forecast_weights)
print("\n[9] Sales Matrix (Product Category x Quarter):")
print(pivot)
print("\n    Forecast Weight Matrix:")
print(forecast_weights)
print("\n    Forecasted Sales:")
print(np.round(forecasted, 2))
print("\n" + "=" * 55)
print("END OF ANALYSIS")
print("=" * 55)
