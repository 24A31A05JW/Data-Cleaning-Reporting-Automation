import pandas as pd

df = pd.read_csv("data/sales_data.csv")

print("Original Data")
print(df)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())

print("\nCleaned Data")
print(df)
df.to_csv(
    "reports/cleaned_report.csv",
    index=False
)

print("Report saved successfully!")
import matplotlib.pyplot as plt

sales_summary = df.groupby(
    "Product"
)["Sales"].sum()

sales_summary.plot(kind="bar")

plt.title("Sales Summary by Product")

plt.savefig(
    "images/sales_summary.png"
)

plt.show()