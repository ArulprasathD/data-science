from database import insert_employees
from employees import employees_details



def main():

    name,salary = employees_details()

    insert_employees(name,salary)



if __name__ == "__main__":
    main()