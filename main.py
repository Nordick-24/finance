import telebot
import psycopg2
from config import host, user, password, db_name

def insert_function(table_name):
    price = input(f"How much money you lose for a {table_name}\n")
    date = input("What date is it?\n")
    
    cursor.execute(f"insert into {table_name} (price, date) values ('{price}', '{date}')")

def look_function(table_name1):
    cursor.execute(f"select * from {table_name1}")
    row = cursor.fetchall()
    
    print("('date'), ('price')")
    for data in row:
        print(data)

try:
    """Connect to database"""
    database = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
                )
    database.autocommit = True
    cursor = database.cursor()

    actions = int(input("""
    What spending do you have?:
    \n1)Apartament
    \n2)Car
    \n3)Clothings
    \n4)Restaurant
    \n5)Look some
    \nWhich One: """))

    if actions == 1:
        insert_function('apartament')

    elif actions == 2:
        insert_function('car')

    elif actions == 3:
        insert_function('clothings')

    elif actions == 4:
        insert_function('reastaurants')

    elif actions == 5:

        which_one = int(input("""What do you want look
        \n1)Apartament
        \n2)Car
        \n3)Clothings
        \n4)Restaurant
        \nWhich one: """))

        if which_one == 1:
            look_function('apartament')

        elif which_one == 2:
            look_function('car')

        elif which_one == 3:
            look_function('clothings')

        elif which_one == 4:
            look_function('reastaurants')

except Exception as _ex:
    print(_ex)

finally:
    cursor.close()
    database.close()
