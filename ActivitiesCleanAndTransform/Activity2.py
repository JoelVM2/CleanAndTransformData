import pandas as pd
students = pd.DataFrame({
    "Name": ["Ana", "Juan", "María", "Pedro"],
    "Age": [20, 21, 22, 22],
    "Grade": [8.5, 7.0, 6.5, 9.0]
})

students["Result"] = students["Grade"].apply(lambda x: "Pass" if x >= 5 else "Fail")
print("\nWith 'Result' column:\n", students)

sales = pd.DataFrame({
    "Product": ["A", "B", "C", "D", "E"],
    "Quantity": [5, 12, 8, 20, 3],
    "Price": [10.0, 5.0, 7.5, 12.0, 9.0]
})

filtered_sales = sales[sales["Quantity"] > 10]
print("\nProducts with more than 10 units sold:\n", filtered_sales)

sorted_students = students.sort_values(by="Grade", ascending=False)
print("\nStudents sorted by grade (descending):\n", sorted_students)
