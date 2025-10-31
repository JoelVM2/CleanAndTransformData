import pandas as pd

df = pd.read_csv("ActivitiesCleanAndTransform/customer_data.csv")

print("\nOriginal data (first 5 rows):\n", df.head())

print("\nNull values per column:\n", df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())

df = df.dropna(subset=["AnnualIncome", "SpendingScore"])

df["AnnualIncome"] = df["AnnualIncome"].astype(float)
df["SpendingScore"] = df["SpendingScore"].astype(float)
df["Age"] = df["Age"].astype(int)

def income_category(income):
    if income >= 25000:
        return "High"
    elif income >= 20000:
        return "Medium"
    else:
        return "Low"

df["IncomeCategory"] = df["AnnualIncome"].apply(income_category)

df["AgeGroup"] = pd.cut(df["Age"], bins=[0,25,45,65,100], labels=["Young","Adult","Mature","Senior"])

print("\nData with new columns (first 5 rows):\n", df.head())

df.to_csv("customer_data_clean.csv", index=False)
print("\nExported cleaned data to 'customer_data_clean.csv'.")
