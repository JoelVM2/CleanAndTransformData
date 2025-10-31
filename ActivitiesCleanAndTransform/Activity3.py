import pandas as pd

students_df = pd.read_csv("ActivitiesCleanAndTransform/students.csv")
print("Primeras 5 filas de students.csv:\n", students_df.head())

clean_students_df = students_df.dropna()
clean_students_df.to_csv("clean_students.csv", index=False)
print("\nArchivo 'clean_students.csv' creado con éxito.")

grades_df = pd.read_csv("ActivitiesCleanAndTransform/grades.csv")

merged_df = pd.merge(clean_students_df, grades_df, on="Name")
print("\nDatos fusionados (students + grades):\n", merged_df)