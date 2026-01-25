import sqlite3
import hashlib

def run():
    login1 = input("Enter your login: ")
    password1 = input("Enter your password: ")

    con = sqlite3.connect("users.db")
    cursor = con.cursor()

    cursor.execute("SELECT salt, password_hash FROM users WHERE login = ?", 
      (login1,)
    )
    row = cursor.fetchone()
    con.close()

    if row is None:
        print("User not found!")
    else:
       salt, stored_hash = row


    input_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password1.encode(),
        salt,
        100_000
     )

    if input_hash == stored_hash:
        print("You are registred" + login1)
    else:
       print("Incorrect data!")

if __name__ == "__main__":
    run()