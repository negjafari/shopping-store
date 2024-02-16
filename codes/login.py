import bcrypt
import mysql.connector
import pickle


class User:
    def __init__(self, user_id, role, fullname, username):
        self.user_id = user_id
        self.role = role
        self.fullname = fullname
        self.username = username

    def __str__(self):
        return self.user_id + " " + self.role + " " + self.username + " " + self.fullname


def password_check(username, password):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT password FROM users WHERE username = " + "'" + username + "'")

    string_hashed_pass = mycursor.fetchall()

    if username == "admin":
        if string_hashed_pass[0][0] == password:
            return True
        else:
            print("incorrect password -admin-")
    else:
        byte_hashed_pass = str.encode(string_hashed_pass[0][0])

        byte_pass = str.encode(password)

        matched = bcrypt.checkpw(byte_pass, byte_hashed_pass)

        if matched:
            return True
        else:
            print("incorrect password")
            return False


def access_check(username, role):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT role FROM users WHERE username = " + "'" + username + "'")

    myresult = mycursor.fetchall()

    if myresult[0][0] == role:
        return True
    else:
        print("role doesn't match")
        return False


def login_validation(username, password, role):
    role_check = access_check(username, role)
    pass_check = password_check(username, password)

    return role_check and pass_check


def get_current_user_data(username):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT user_id, role, full_name FROM users WHERE username = " + "'" + username + "'")

    myresult = mycursor.fetchall()

    mydb.commit()

    return myresult


def save_current_user_data(username):
    res = get_current_user_data(username)
    user = User(str(res[0][0]), str(res[0][1]), res[0][2], username)
    file = open("user.b", "wb")

    pickle.dump(user, file)
    print("user data saved")
    file.close()


def load_current_user_data():
    try:
        file_pi2 = open('user.b', 'rb')
        object_pi2 = pickle.load(file_pi2)
        return object_pi2
    except IOError:
        print("could not open file")
        return []





