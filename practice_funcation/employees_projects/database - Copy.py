import mysql.connector


def insert_employees(name,salary):

    connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "employees_db"
    )
    

    cursor = connection.cursor()

    query = """
    INSERT INTO employees(name,salary)
    VALUES(%s,%s)
    """

    values = (name,salary)

    cursor.execute(query,values)

    print("employees details added successfully!")

    connection.commit()
    cursor.close()
    connection.close()