"""
Output Module - grade_checker_output.py
Handles all output and display formatting for the Grade Checker program.
"""


def display_student_results(students):
    """Display grades for all students in a formatted table."""
    print("\n" + "=" * 70)
    print(f"{'Student Name':<20} {'Numeric Grade':<15} {'Letter Grade':<15} {'GPA Points':<10}")
    print("=" * 70)
    
    for student in students:
        name = student["name"]
        numeric = f"{student['grade']:.2f}"
        letter = student["letter_grade"]
        gpa = f"{student['gpa_points']:.2f}"
        
        print(f"{name:<20} {numeric:<15} {letter:<15} {gpa:<10}")
    
    print("=" * 70)


def display_class_statistics(students, class_avg, class_gpa):
    """Display class-wide statistics."""
    print("\nClass Statistics:")
    print("-" * 40)
    print(f"Class Average Grade: {class_avg:.2f}")
    print(f"Class Average GPA: {class_gpa:.2f}")
    print("-" * 40)


def display_welcome_message():
    """Display welcome message."""
    print("Welcome to the Grade Checker Program!")
    print("-" * 40)


def display_goodbye_message():
    """Display goodbye message."""
    print("\nThank you for using the Grade Checker Program!")


def display_no_students_message():
    """Display message when no students were added."""
    print("No students were added.")
