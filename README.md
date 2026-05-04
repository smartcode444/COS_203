# Grade Checker Program

This repository contains two implementations of a Grade Checker program in Python:
1. **Single File Version** - All functions in one file
2. **Modular Version** - Code organized into separate modules

## Version 1: Single File Grade Checker

**File:** `grade_checker_single_file.py`

This version contains all functions in a single Python file with clear separation of concerns.

### Features:
- Input validation for student count and grades
- Conversion of numeric grades to letter grades (A-F)
- GPA calculation (4.0 scale)
- Class average and GPA statistics
- Formatted output table

### How to Run:
```bash
python grade_checker_single_file.py
```

### Functions in Single File:
- `get_student_count()` - Gets number of students
- `get_student_info()` - Gets individual student name and grade
- `get_all_students()` - Collects all student data
- `convert_to_letter_grade()` - Converts numeric to letter grade
- `calculate_gpa_points()` - Converts letter grade to GPA points
- `process_grades()` - Processes all grades
- `calculate_class_average()` - Calculates class average
- `calculate_class_gpa()` - Calculates class GPA
- `display_student_results()` - Displays formatted results
- `display_class_statistics()` - Shows class statistics
- `main()` - Main program flow

---

## Version 2: Modular Grade Checker

This version separates the program into four focused modules:

**Files:**
- `grade_checker_main.py` - Main module (orchestrator)
- `grade_checker_input.py` - Input module
- `grade_checker_logic.py` - Logic/calculation module
- `grade_checker_output.py` - Output/display module

### Module Structure:

#### `grade_checker_input.py`
Handles all user input:
- `get_student_count()` - Validates student count
- `get_student_info()` - Gets student name and grade
- `get_all_students()` - Collects all student data

#### `grade_checker_logic.py`
Handles all calculations and processing:
- `convert_to_letter_grade()` - Grade conversion
- `calculate_gpa_points()` - GPA conversion
- `process_grades()` - Process all grades
- `calculate_class_average()` - Class average
- `calculate_class_gpa()` - Class GPA

#### `grade_checker_output.py`
Handles all display and formatting:
- `display_student_results()` - Results table
- `display_class_statistics()` - Statistics display
- `display_welcome_message()` - Welcome message
- `display_goodbye_message()` - Goodbye message
- `display_no_students_message()` - No students message

#### `grade_checker_main.py`
Orchestrates the program:
- `main()` - Imports and coordinates all modules

### How to Run:
```bash
python grade_checker_main.py
```

**Note:** When running the modular version, ensure all four module files are in the same directory.

---

## Grade Conversion Scale

| Letter Grade | Numeric Range | GPA Points |
|--------------|---------------|-----------|
| A            | 90-100        | 4.0       |
| B            | 80-89         | 3.0       |
| C            | 70-79         | 2.0       |
| D            | 60-69         | 1.0       |
| F            | 0-59          | 0.0       |

---

## Example Usage

```
Welcome to the Grade Checker Program!
----------------------------------------
How many students do you want to grade? 3
Enter name for student 1: Alice
Enter grade for Alice (0-100): 92
Enter name for student 2: Bob
Enter grade for Bob (0-100): 78
Enter name for student 3: Charlie
Enter grade for Charlie (0-100): 85

======================================================================
Student Name         Numeric Grade   Letter Grade    GPA Points
======================================================================
Alice                92.00           A               4.00
Bob                  78.00           C               2.00
Charlie              85.00           B               3.00
======================================================================

Class Statistics:
----------------------------------------
Class Average Grade: 85.00
Class Average GPA: 3.00
----------------------------------------

Thank you for using the Grade Checker Program!
```

---

## Comparison of Approaches

| Aspect | Single File | Modular |
|--------|------------|---------|
| Complexity | Simple, all-in-one | Organized, separated concerns |
| Reusability | Functions can be imported | Modules can be reused independently |
| Testing | Easier for small programs | Easier for large programs |
| Maintainability | Suitable for learning | Better for larger projects |
| Scalability | Limited | Highly scalable |

---

## Requirements
- Python 3.6+
- No external libraries required

---

## Author
Created as a classwork assignment to demonstrate function organization and modular programming principles in Python.
