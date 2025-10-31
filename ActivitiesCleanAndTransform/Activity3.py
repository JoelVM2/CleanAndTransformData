import pandas as pd

students = pd.DataFrame({
    "Name": ["Ana", "Juan", "María", "Pedro"],
    "Age": [20, 21, 22, 22],
    "Grade": [8.5, 7.0, 6.5, 9.0]
})
students.to_csv("students.csv", index=False)

csv_df = pd.read_csv("students.csv")
print("\nFirst 5 rows of CSV:\n", csv_df.head())

clean_csv = csv_df.dropna()
clean_csv.to_csv("clean_students.csv", index=False)
print("\nFile created successfully.")

students_info = pd.DataFrame({
    "Name": ["Ana", "Juan", "María", "Pedro"],
    "Age": [20, 21, 22, 22],
    "Class": ["A", "B", "A", "B"]
})
grades = pd.DataFrame({
    "Name": ["Ana", "Juan", "María", "Pedro"],
    "Grade": [8.5, 7.0, 6.5, 9.0]
})

merged_df = pd.merge(students_info, grades, on="Name")
print("\nMerged data (students + grades):\n", merged_df)
