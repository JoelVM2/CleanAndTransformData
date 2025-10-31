import pandas as pd

data = {
    "Name": ["Ana", "Juan", "María", "Pedro", None, "Juan"],
    "Age": [20, 21, None, 22, 21, 21],
    "Grade": [8.5, 7.0, 6.5, None, 9.0, 7.0],
    "Price": ["12.5", "8.0", None, "10.0", "9.5", "8.0"]
}

df = pd.DataFrame(data)
print("\nOriginal data:\n", df)

df_sin_nulos = df.dropna()
print("\nWithout Null:\n", df_sin_nulos)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Grade"] = df["Grade"].fillna(df["Grade"].mean())
df["Price"] = df["Price"].fillna("0")

df = df.drop_duplicates()
df["Price"] = df["Price"].astype(float)

media_precio = df["Price"].mean()
print("\nAverage Price:", media_precio)

print("\nClean Data:\n", df)
