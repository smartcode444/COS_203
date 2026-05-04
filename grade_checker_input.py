"""
Input Module - grade_checker_input.py
Handles all user input for the Grade Checker program.
"""


def get_student_count():
    """Get the number of students from user input."""
    while True:
        try:
            count = int(input("How many students do you want to grade? "))
            if count <= 0:
                print("Please enter a positive number.")
                continue
            return count
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_student_info(student_num):
    """Get name and grade for a single student."""
    name = input(f"Enter name for student {student_num}: ").strip()
    
    while True:
        try:
            grade = float(input(f"Enter grade for {name} (0-100): "))
            if grade < 0 or grade > 100:
                print("Grade must be between 0 and 100.")
                continue
            return name, grade
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_all_students():
    """Get information for all students."""
    count = get_student_count()
    students = []
    
    for i in range(1, count + 1):
        name, grade = get_student_info(i)
        students.append({"name": name, "grade": grade})
    
    return students
