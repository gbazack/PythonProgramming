## Practice Exam 1: School Management System

In this practice exam, you will implement a school management system with Python data structures such as list and dictionary and interact with it via functions. More precisely, you'll:
1. Create databases:
   1. A database to save students’ information (ID, names, age, level, sex.)
   2. A database to save teacher’s information such as his/her ID, name, age, sex, course ID.
   3. A database to register courses described by an ID, title, category, lecturer ID.
   4. A database to save the notes with the following attributes: Note ID, student ID, Course ID, and values.
   
   Identification number (ID) should be of type string, and each database should contain at least 10 items.
   
2. Manipulate these databases:
   1. Search items from:
      1. implement functions to get the ID of any item from a database
      2. implement a function to get a note of a student for a specific course
      3. implement a function to get the categories of all courses attended by a student
   2. Add items to:
      1. implement a function to add the attributes 'income' and 'skills' to teachers' database
      2. implement a function to add the attributes 'course credit' and 'grade' to notes' database
      3. implement functions to add a note, and a student
   3. Remove items from
      1. implement a function to remove a teacher
   4. Modify items of
      1. implement a function to compute a student overall grade
      2. implement a function to edit a student's names
