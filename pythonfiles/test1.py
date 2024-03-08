#connecting to database with sqllite

import sqlite3

connection = sqlite3.connect("tmrktdb_test")

#cursor object to execute sql

cursor = connection.cursor()

#db table schema

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL
    )
''')

#COMMIT CHANGES
connection.commit()

#insert dummy data

users_data =[("User_1",), ("User_2",), ("User_3",)]
cursor.executemany("INSERT INTO USERS (username) VALUES (?)", users_data)

#COMMIT CHANGES
connection.commit()

#get users from db
def get_new_users_from_db(num_users):
    cursor.execute("SELECT id, username FROM users LIMIT ?", (num_users))
    return cursor.fetchall()

#closeconnection
connection.close()


def send_message(user_id, message):
    print("PLay this now @ 0.11")

def main():
    connection = sqlite3.connect("tmrktdb_test")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL
        )
    ''')

    #COMMIT CHANGES
    connection.commit()

    initial_users = 1
    exponent_factor = 3

    for i in range(1,6):
        new_users = get_new_users_from_db(initial_users, cursor)

        for user_id, username in new_users:
            send_message(user_id, "Dawg play the game")

        intitial_users *= exponent_factor

    connection.close()

if __name__ == "__main__":
    main()

