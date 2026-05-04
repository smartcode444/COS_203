"""
Main Module - grade_checker_main.py
Orchestrates the Grade Checker program by importing and using all modules.
"""

from grade_checker_input import get_all_students
from grade_checker_logic import process_grades, calculate_class_average, calculate_class_gpa
from grade_checker_output import (
    display_welcome_message,
    display_student_results,
    display_class_statistics,
    display_goodbye_message,
    display_no_students_message
)


def main():
    """Main function to run the grade checker program."""
    display_welcome_message()
    
    students = get_all_students()
    
    if not students:
        display_no_students_message()
        return
    
    process_grades(students)
    display_student_results(students)
    
    class_avg = calculate_class_average(students)
    class_gpa = calculate_class_gpa(students)
    display_class_statistics(students, class_avg, class_gpa)
    
    display_goodbye_message()


if __name__ == "__main__":
    main()
