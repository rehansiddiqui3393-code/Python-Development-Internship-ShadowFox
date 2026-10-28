# Section 7: File Handling
import csv

# 1. Open the file in read mode and create a dictionary from the data
students = {}
with open("student_marks.csv", "r") as file:
    reader = csv.DictReader(file)
    subjects = [col for col in reader.fieldnames if col not in ("Name", "Roll_No")]
    for row in reader:
        students[row["Roll_No"]] = {
            "Name": row["Name"],
            **{sub: int(row[sub]) for sub in subjects}
        }

# 2 & 3. Add total_marks and Average fields
for roll, data in students.items():
    total = sum(data[sub] for sub in subjects)
    data["total_marks"] = total
    data["Average"] = round(total / len(subjects), 2)

# 4. Write the information to a new text file
with open("student_report.txt", "w") as out:
    for roll, data in students.items():
        out.write(f"Roll {roll}: {data}\n")
print("Created student_report.txt")

# Q2: Create a new CSV file with total marks and average marks
with open("student_marks_with_total.csv", "w", newline="") as out:
    fieldnames = ["Name", "Roll_No"] + subjects + ["total_marks", "Average"]
    writer = csv.DictWriter(out, fieldnames=fieldnames)
    writer.writeheader()
    for roll, data in students.items():
        row = {"Roll_No": roll}
        row.update(data)
        writer.writerow(row)
print("Created student_marks_with_total.csv")

for roll, data in students.items():
    print(roll, data["Name"], data["total_marks"], data["Average"])
