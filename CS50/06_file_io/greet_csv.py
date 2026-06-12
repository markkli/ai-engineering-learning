import csv

students = []

with open("06_file_io/names.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"].title(), "house": row["house"].title()})

"""
def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name, reverse=True):
    print(f"Hello, {student['name']} from {student['house']}!")
"""

for student in sorted(students, key=lambda student: student["name"]):
    print(f"Hello, {student['name']} from {student['house']}!") 