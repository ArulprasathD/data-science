"""
Welcome message.
Available movies display pannu.
User movie select pannanum.
Invalid movie na thirumba kekkanum.
Number of tickets kekkanum.
Total bill calculate pannanum.
Booking details print pannanum.
"Need another booking?" nu kekkanum.
yes na first step-ku poganum.
no na:
All booked movies print pannanum.
Grand total print pannanum.
Thank you message kaatanum
"""

import backend as bd

def Greeting():
    return "welcome !!"

def Avl_tickets():
    return bd.available_tickets()

def avl_movies():
    for i in bd.movies_(bd.MOVIES()):
        print(i)


def user(movie):
    if movie == bd.movies_(bd.MOVIES["kara"]):
        return f"selected movie : kara "
    

def main ():

    print(Greeting())
    print(Avl_tickets())
    print(avl_movies())
    movie = input("select movies would you like to watch : ")
    print(user(movie))



if __name__ == "__main__":
    main()
    