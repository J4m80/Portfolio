import hashlib
import os
import sqlite3

def run():
    login = input("Write your login:")
    password = input("Write your password:")

    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)

    con = sqlite3.connect("users.db")
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        login TEXT UNIQUE,
        salt BLOB,
        password_hash BLOB
    )""")
    con.commit()

    cursor.execute("INSERT INTO users VALUES(?,?,?)",
        (login, salt, password_hash)           
    )
    con.commit()
    print("You have been registered!")

if __name__ == "__main__":
    run()