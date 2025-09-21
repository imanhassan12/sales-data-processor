import os
import pandas as pd
import matplotlib.pyplot as plt

print("✅ Starting Sales Data Processor...")

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root
DATA_PATH = os.path.join(BASE_DIR, "data", "sales.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
SUMMARY_CSV = os.path.join(OUTPUT_DIR, "summary.csv")
PLOT_PATH = os.path.join(OUTPUT_DIR, "sales_report.png")
os.makedirs(OUTPUT_DIR, exist_ok=True)

print(f"• Reading CSV from: {DATA_PATH}")

# --- Load & validate ---
df = pd.read_csv(DATA_PATH)
print("• Preview:")
print(df.head())

# --- Clean ---
df = df.dropna()
print(f"• Rows after dropna: {len(df)}")

# --- Aggregate ---
sales_by_product = (
    df.groupby("Product", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)
)
print("\n• Total Sales by Product:")
print(sales_by_product)

# --- Save summary table ---
sales_by_product.to_csv(SUMMARY_CSV, index=False)
print(f"• Summary saved to: {SUMMARY_CSV}")

# --- Plot ---
plt.figure(figsize=(8, 5))
plt.bar(sales_by_product["Product"], sales_by_product["Sales"])
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(PLOT_PATH, dpi=150)
plt.close()
print(f"• Chart saved to: {PLOT_PATH}")

print("🎉 Done.")
