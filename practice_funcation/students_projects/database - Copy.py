import mysql.connector


def insert_student(name,age):


    connection = mysql.connector.connect(
        host = "localhost",
        user = 'root',
        password = "root",
        database = "student_db"
    )

    cursor = connection.cursor()


    query = """
    INSERT INTO students(name, age)
    VALUES(%s, %s)
    """


    values = (name,age)

    cursor.execute(query,values)

    connection.commit()


    print("student added successfully!")

    cursor.close()
    connection.close()


