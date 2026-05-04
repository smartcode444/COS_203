"""
Logic Module - grade_checker_logic.py
Handles all grade processing and calculations for the Grade Checker program.
"""


def convert_to_letter_grade(grade):
    """Convert numeric grade to letter grade."""
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'


def calculate_gpa_points(letter_grade):
    """Convert letter grade to GPA points (4.0 scale)."""
    gpa_scale = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    return gpa_scale.get(letter_grade, 0.0)


def process_grades(students):
    """Process grades and add letter grades and GPA points."""
    for student in students:
        grade = student["grade"]
        letter_grade = convert_to_letter_grade(grade)
        gpa_points = calculate_gpa_points(letter_grade)
        
        student["letter_grade"] = letter_grade
        student["gpa_points"] = gpa_points


def calculate_class_average(students):
    """Calculate the average grade for the class."""
    if not students:
        return 0
    
    total = sum(student["grade"] for student in students)
    return total / len(students)


def calculate_class_gpa(students):
    """Calculate the average GPA for the class."""
    if not students:
        return 0.0
    
    total_gpa = sum(student["gpa_points"] for student in students)
    return total_gpa / len(students)
