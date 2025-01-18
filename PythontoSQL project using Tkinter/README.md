# Student Registration System - Python to SQL using Tkinter

The Student Registration System is a GUI application created with Python and tkinter. It is designed to manage student data for a course enrollment. This version of the system utilizes a MySQL database to store and retrieve student information, such as id, name, course, fee etc.,

# Description: 

* The Advanced Student Management System is a comprehensive application developed using Tkinter and MySQL database. 
* It provides functionalities for managing student records efficiently. 
* The system allows users to add new students, delete existing students, update student information, and search for student records based on various criteria. The application offers a user-friendly interface with intuitive controls for seamless data management.
  
# Features:

* Add Student: Allows the user to add a student with their name, course, and fee to the database.
* Update Student: Allows the user to update a student's information by selecting them from a list.
* Delete Student: Allows the user to delete a student's record by selecting them from the list.
* View Students: Displays all student records from the database in a table-like format using Tkinter's Treeview widget.
* Refresh: Clears the input fields after operations.
* Exit: Close the application with a confirmation prompt.

# Install Dependencies
* Use the following command to install the required dependencies:

pip install mysql-connector-python

# Database Setup
* Create Database: Open MySQL Workbench or any MySQL client and create a database called webgui.

CREATE DATABASE webgui;

* Create Table: In the webgui database, create a table called registration to store student data. The table structure should look like this:

CREATE TABLE registration (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    course VARCHAR(255) NOT NULL,
    fee DECIMAL(10, 2) NOT NULL
);

* Configure Database Connection: Ensure the database credentials in the Python script match your MySQL setup. The script uses:


host='localhost',
user='root',
password='1234',
database='webgui'

* Modify the get_db_connection() function if necessary.

# Technologies: 

* Python
* Tkinter
* MySQL


![image](https://github.com/user-attachments/assets/35a4f17e-28a5-4eee-8910-61f431b9fdad)
