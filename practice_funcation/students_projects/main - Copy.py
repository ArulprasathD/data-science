from student import student_details
from database import insert_student

def main():

    name,age = student_details()
    insert_student(name,age)



if __name__ == "__main__":
    main()