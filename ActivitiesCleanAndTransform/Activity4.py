import pandas as pd

class_grades = pd.DataFrame({
    "Name": ["Ana", "Juan", "María", "Pedro", "Luis"],
    "Grade": [9.2, 7.5, 5.0, 4.3, 8.8]
})

print("\nAverage:", class_grades["Grade"].mean())
print("Max:", class_grades["Grade"].max())
print("Min:", class_grades["Grade"].min())

def category(grade):
    if grade >= 9:
        return "Excellent"
    elif grade >= 7:
        return "Good"
    elif grade >= 5:
        return "Pass"
    else:
        return "Fail"

class_grades["Category"] = class_grades["Grade"].apply(category)
print("\nGrades with categories:\n", class_grades)

sales = pd.DataFrame({
    "Product": ["A", "B", "C", "D", "E"],
    "Quantity": [10, -5, 15, 0, 8],
    "Price": [10.0, 5.0, 7.5, 12.0, 9.0],
    "Date": ["2025-10-01", "2025-10-02", "", "2025-10-03", "2025-10-04"]
})

sales = sales[(sales["Quantity"] > 0) & (sales["Date"] != "")]
sales["Total"] = sales["Quantity"] * sales["Price"]

print("\nTotal sales per product:\n", sales[["Product", "Total"]])
