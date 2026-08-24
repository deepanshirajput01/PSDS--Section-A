import mysql.connector

# Connect Python to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger"
)

cursor = connection.cursor()

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS CampusDB")

cursor.execute("USE CampusDB")

#Faculty table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Faculty (
    faculty_id INT PRIMARY KEY,
    faculty_name VARCHAR(100) NOT NULL
)
""")

#Learner table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Learner (
    learner_id INT PRIMARY KEY,
    learner_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    faculty_id INT,
    FOREIGN KEY (faculty_id)
    REFERENCES Faculty(faculty_id)
)
""")

#Subject table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Subject (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL,
    credits INT,
    faculty_id INT,
    FOREIGN KEY (faculty_id)
    REFERENCES Faculty(faculty_id)
)
""")

#Registration table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Registration (
    registration_id INT PRIMARY KEY,
    learner_id INT,
    subject_id INT,
    registration_date DATE,
    FOREIGN KEY (learner_id)
    REFERENCES Learner(learner_id),
    FOREIGN KEY (subject_id)
    REFERENCES Subject(subject_id)
)
""")

connection.commit()

print("Database CampusDB created successfully!")
print("All tables created successfully!")

cursor.close()
connection.close()