# try:
#     conn = psycopg.connect("dbname = your_dbname user=your_username password = your_password host=your_host port=your_port")
# except psycopg.OperationalErrorase as e:
#     print(f"Error:{e}")
#     exit(1)

# with conn.cursor() as cursor:

# cursor.execute("SELECT * FROM yourtable")

# rows = cursor.fetchall()
# for row in rows:
#     print(row)

import getpass
word = getpass.getpass("Enter your postgres password: ")
import psycopg2

def getAllStudents():
    conn = None
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(f"dbname=A3Q1 user=postgres password={word} host=::1 port=5432")

        # Create a cursor
        with conn.cursor() as cursor:
            # Execute the SQL command to retrieve all students
            cursor.execute("SELECT * FROM students ORDER BY student_id")

            # Fetch all the rows
            rows = cursor.fetchall()

            # Display the results
            for row in rows:
                print(row)

    except psycopg2.OperationalError as e:
        print(f"Error: {e}")
    # finally:
    #     # Close the connection
    #     if conn:
    #         conn.close()

# Call the function
# getAllStudents()


def addStudent(first_name, last_name, email, enrollment_date):

    conn = None
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(f"dbname=A3Q1 user=postgres password={word} host=::1 port=5432")

        # Create a cursor
        with conn.cursor() as cursor:
            query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"

            # Provide values as a tuple to prevent SQL injection
            values = (first_name, last_name, email, enrollment_date)

            # Execute the SQL command
            cursor.execute(query, values)
        conn.commit()
        print("Student added successfully!")

    except psycopg2.OperationalError as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()

#addStudent('Bob', 'Coe', 'bob.coe@gmail.com', '2024-09-01')


def updateStudentEmail(student_id, new_email):
    conn = None
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(f"dbname=A3Q1 user=postgres password={word} host=::1 port=5432")

        # Create a cursor
        with conn.cursor() as cursor:
            query = "UPDATE students SET email = %s WHERE student_id = %s"

            # Provide values as a tuple to prevent SQL injection
            values = (new_email, student_id)

            # Execute the SQL command
            cursor.execute(query, values)
        conn.commit()
        print("Student email changed successfully!")

    except psycopg2.OperationalError as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()

# updateStudentEmail(1, 'gmail')

def deleteStudent(student_id):

    conn = None
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(f"dbname=A3Q1 user=postgres password={word} host=::1 port=5432")

        # Create a cursor
        with conn.cursor() as cursor:
            query = "DELETE FROM students WHERE student_id = %s"
            values = (student_id,)
            # Execute the SQL command
            cursor.execute(query, values)
        conn.commit()
        print("Student deleted successfully!")

    except psycopg2.OperationalError as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()

# deleteStudent(4)


def main():
    while (True):
        print("\nEnter 1 to call getAllStudents")
        print("Enter 2 to call addStudent")
        print("Enter 3 to call updateStudentEmail")
        print("Enter 4 to call deleteStudent")
        print("Enter 0 to end program")
        selection = input("Make a selection: ")
        if(selection=='1'):
            getAllStudents()
        elif(selection=='2'):
            first_name=input("What is the student's first name: ")
            last_name=input("What is the student's last name: ")
            email=input("What is the student's email: ")
            enrollment_date=input("What is the student's enrollment date: ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif(selection=='3'):
            student_id=input("What is the student's id you wish to update their email: ")
            new_email=input("What is the student's new email: ")
            updateStudentEmail(student_id, new_email)
        elif(selection=='4'):
            student_id=input("What is the student's id you wish to delete: ")
            deleteStudent(student_id)
        elif(selection=='0'):
            break

main()
