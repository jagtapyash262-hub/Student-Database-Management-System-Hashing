# Student Database Management System using Hashing

## Mini Project – Data Structures

A menu-driven Python mini project that manages student records using a hash table. Each student is identified by a unique roll number. The hash function maps a roll number to a table index, and collisions are handled using **separate chaining**.

## Features

- Add a student
- Search by roll number
- Update student details
- Delete a student
- Display all student records
- Display the hash table and its buckets
- Prevent duplicate roll numbers
- Validate roll numbers and marks
- Handle collisions with separate chaining

## Technologies Used

- Python 3
- Hash Table
- Hash Function
- Separate Chaining
- Lists and Dictionaries

## Project Structure

```text
Student-Database-Management-System-Hashing/
├── student_database.py
├── README.md
└── output/
    └── sample_output.txt
```

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python student_database.py
```

On some Windows installations, use:

```bash
py student_database.py
```

## Hashing Logic

The hash function is:

```python
index = roll_no % TABLE_SIZE
```

The table size is `10`. For example, roll numbers `101` and `111` both map to index `1`. This is a collision. The program stores both records in the same bucket using separate chaining.

## Sample Test Data

| Roll Number | Name | Course | Marks |
|---:|---|---|---:|
| 101 | Aditi Sharma | BSc CS | 85 |
| 111 | Rohan Patil | BSc CS | 90 |
| 102 | Neha Joshi | BCA | 78.5 |

Roll numbers `101` and `111` collide at hash index `1`.

## Time Complexity

| Operation | Average Case | Worst Case |
|---|---:|---:|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Update | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Display all records | O(n) | O(n) |

Average-case performance depends on a good distribution of keys and the load on each bucket. If many keys map to the same bucket, operations can take O(n).

## Limitations

- Records are stored in memory and are cleared when the program exits.
- This is an educational console application, not a production database.

## Future Enhancements

- Save records to a file so they persist after restarting.
- Add department, semester, email, and attendance fields.
- Create a graphical user interface.
- Export student records to CSV.

## Conclusion

This project demonstrates how hashing can provide efficient student-record lookup. Separate chaining handles collisions by storing multiple records in a bucket.

## Author

Add your name, class, roll number, and academic year here before submitting.
