# Task 1: Grade Checker
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

print("\nStudent Grades Dictionary")

# Task 2: Student Grades
students = {}

n = int(input("How many students do you want to add? "))

for i in range(n):
    name = input("Enter student name: ")
    grade = input("Enter grade: ")
    students[name] = grade

update = input("Enter student name to update: ")

if update in students:
    new_grade = input("Enter new grade: ")
    students[update] = new_grade
else:
    print("Student not found.")

print("\nAll Student Grades")

for name, grade in students.items():
    print(name, ":", grade)

# Task 3: Write to File
file = open("sample.txt", "w")
file.write("Hello!\n")
file.write("This file was created using Python.\n")
file.close()

print("\nData written to sample.txt")

# Task 4: Read from File
file = open("sample.txt", "r")
content = file.read()
file.close()

print("\nContents of sample.txt")
print(content)