# MINI PROJECT: STUDENT DATABASE MANAGEMENT SYSTEM
# Concept: Hashing (Hash Table with Separate Chaining)
# Storage: In-memory dictionary and lists

TABLE_SIZE = 10
hash_table = [[] for _ in range(TABLE_SIZE)]


def hash_function(roll_no):
    """Map a student roll number to a hash table index."""
    return roll_no % TABLE_SIZE


def find_student(roll_no):
    """Return (bucket_index, student_record) if found, otherwise (index, None)."""
    index = hash_function(roll_no)
    for student in hash_table[index]:
        if student["roll_no"] == roll_no:
            return index, student
    return index, None


def add_student():
    try:
        roll_no = int(input("Enter Roll Number: "))
        if roll_no <= 0:
            print("Roll number must be a positive integer.")
            return
        index, existing = find_student(roll_no)
        if existing:
            print("A student with this roll number already exists.")
            return

        name = input("Enter Student Name: ").strip()
        course = input("Enter Course: ").strip()
        marks = float(input("Enter Marks (0-100): "))
        if not name or not course:
            print("Name and course cannot be empty.")
            return
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        student = {
            "roll_no": roll_no,
            "name": name,
            "course": course,
            "marks": marks
        }
        hash_table[index].append(student)
        print(f"Student added successfully at hash index {index}!")
    except ValueError:
        print("Invalid input. Please enter a valid roll number and marks.")


def search_student():
    try:
        roll_no = int(input("Enter Roll Number to Search: "))
        index, student = find_student(roll_no)
        if student:
            print("\nStudent Record Found")
            print(f"Hash Index : {index}")
            print(f"Roll Number: {student['roll_no']}")
            print(f"Name       : {student['name']}")
            print(f"Course     : {student['course']}")
            print(f"Marks      : {student['marks']:.2f}")
        else:
            print("Student record not found.")
    except ValueError:
        print("Please enter a valid roll number.")


def update_student():
    try:
        roll_no = int(input("Enter Roll Number to Update: "))
        index, student = find_student(roll_no)
        if not student:
            print("Student record not found.")
            return

        print("Leave a field blank to keep its current value.")
        name = input(f"New Name [{student['name']}]: ").strip()
        course = input(f"New Course [{student['course']}]: ").strip()
        marks_text = input(f"New Marks [{student['marks']:.2f}]: ").strip()

        if name:
            student["name"] = name
        if course:
            student["course"] = course
        if marks_text:
            marks = float(marks_text)
            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100. Update cancelled.")
                return
            student["marks"] = marks

        print("Student record updated successfully.")
    except ValueError:
        print("Invalid marks. Please enter a number between 0 and 100.")


def delete_student():
    try:
        roll_no = int(input("Enter Roll Number to Delete: "))
        index, student = find_student(roll_no)
        if not student:
            print("Student record not found.")
            return
        hash_table[index].remove(student)
        print("Student record deleted successfully.")
    except ValueError:
        print("Please enter a valid roll number.")


def display_students():
    print("\n" + "=" * 72)
    print(f"{'ROLL NO.':<12}{'NAME':<24}{'COURSE':<20}{'MARKS':>8}")
    print("-" * 72)
    count = 0
    for bucket in hash_table:
        for student in bucket:
            print(
                f"{student['roll_no']:<12}"
                f"{student['name']:<24}"
                f"{student['course']:<20}"
                f"{student['marks']:>8.2f}"
            )
            count += 1
    if count == 0:
        print("No student records available.")
    print("-" * 72)
    print(f"Total students: {count}")


def display_hash_table():
    print("\nHASH TABLE (Separate Chaining)")
    print("-" * 60)
    for index, bucket in enumerate(hash_table):
        if bucket:
            records = " -> ".join(
                f"{student['roll_no']} ({student['name']})"
                for student in bucket
            )
            print(f"Index {index}: {records}")
        else:
            print(f"Index {index}: EMPTY")
    print("-" * 60)


def main():
    while True:
        print("\n========== STUDENT DATABASE MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Display Hash Table")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            display_students()
        elif choice == "6":
            display_hash_table()
        elif choice == "7":
            print("Thank you for using Student Database Management System!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 7.")


if __name__ == "__main__":
    main()
