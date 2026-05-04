"""
Grade Checker Program - Single File Version
This program takes student grades and displays them with letter grades.
Functions are broken down into smaller, manageable pieces.
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


def display_class_statistics(students):
    """Display class-wide statistics."""
    class_avg = calculate_class_average(students)
    class_gpa = calculate_class_gpa(students)
    
    print("\nClass Statistics:")
    print("-" * 40)
    print(f"Class Average Grade: {class_avg:.2f}")
    print(f"Class Average GPA: {class_gpa:.2f}")
    print("-" * 40)


def main():
    """Main function to run the grade checker program."""
    print("Welcome to the Grade Checker Program!")
    print("-" * 40)
    
    students = get_all_students()
    
    if not students:
        print("No students were added.")
        return
    
    process_grades(students)
    display_student_results(students)
    display_class_statistics(students)
    
    print("\nThank you for using the Grade Checker Program!")


if __name__ == "__main__":
    main()
