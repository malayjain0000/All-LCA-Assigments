students = {
    1: {
        "Name": "Malay",
        "Branch": "AI & DS",
        "Mark": 85
    },
    2: {
        "Name": "Rahul",
        "Branch": "CSE",
        "Mark": 78
    }
}

# Tuple
student_tuple = (3, "Amit", "IT", 82)

# List
student_list = [4, "Raj", "CSE", 75]

# Add a new student
students[3] = {
    "Name": student_tuple[1],
    "Branch": student_tuple[2],
    "Mark": student_tuple[3]
}

# Delete an existing student
del students[2]

# Update student details
students[1]["Mark"] = 90
students[1]["Branch"] = "AI & DS"

# Display final student records
print("Final Student Records:")

for roll_number, details in students.items():
    print("Roll Number:", roll_number)
    print("Name:", details["Name"])
    print("Branch:", details["Branch"])
    print("Mark:", details["Mark"])
    print()