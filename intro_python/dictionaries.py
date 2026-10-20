
student = {
    "name": "Isaac",
    "age": 24,
    "major": "computer science"
}
"""
print(student)

print(student["major"])
print(student.get("major"))

# print(student["email"])

student["graduation"] = 2027

print(student.get("graduation"))

student["age"] = 28

print(student.get("age"))

student.pop("graduation")

print(student)

if "age" in student:
    print("name exists")

# Nested Dictionaries

students = {
    "student1": {"name": "Isaac", "age": 28, "major": "computer science"},
    "student2": {"name": "Leo", "age": 24, "major": "computer science"}
}

print(students)

print(students["student2"]["name"])

studentss = [
    {"name": "Isaac", "age": 28, "major": "computer science"},
    {"name": "Leo", "age": 24, "major": "computer science"}
]

print(studentss[1]["name"])

for student in studentss:
    print(f"{student['name']} is {student['age']}")

studentss.append({"name": "Noah", "age": 28, "major": "computer science"})
print(len(studentss))

"""

student.update({"age": 19, "gpa": 3.8})
print(student)


"""
MINI CHALLENGE: STUDENT REPORT CARD
You need to store and analyze a student's grades.
1. Create a dictionary called "report_card" with keys:
    -"name"
    - "subject"
    - "grades" (use a tuple with 3 numbers)
Example: {"name": "Leo", "subject": "Math", "grades": (90, 85, 88)}
2. Print the student's name and subject.
3. Calculate the average of the 3 grades (HINT: use sum() and len()).
4. Add a new key called "average" with the calculated result.
5. If the average is 90 or above → print "Excellent!"
    If between 70 and 89 → print "Good job!"
    Otherwise → print "Needs improvement!"
6. Remove the "subject" key and print the updated dictionary.
"""

report_card = {"name": "Isaac", "subject": "Math", "grades": (90, 85, 88)}
print(report_card["name"])
print(report_card["subject"])

average = round(sum(report_card["grades"]) / len(report_card["grades"]), 2)
print(average)

report_card.update({"average": average})

if report_card["average"] > 90:
    print("Excellent!")
elif report_card["average"] >= 70 and report_card["average"] <= 89:
    print("Good job!")
else:
    print("Needs Improvement")

report_card.pop("subject")
print(report_card)