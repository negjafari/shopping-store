import re
from datetime import datetime
import bcrypt
import mysql.connector


def insert_database(dic, table_name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    cursor = mydb.cursor()

    joining_date = datetime.now()

    hashed_pass = get_hashed_password(dic["password"]).decode("utf-8")

    sql = "INSERT INTO " + table_name + " (role, full_name, username, password, email," \
                                        " phone_number, address, postal_code, joining_date," \
                                        " updating_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (dic["role"], dic["full_name"], dic["username"], hashed_pass, dic["email"],
           dic["phone_number"], dic["address"], dic["postal_code"], joining_date, joining_date)

    try:
        cursor.execute(sql, val)
    except mysql.connector.errors.IntegrityError:
        print("username/email already token")
    else:
        print("inserted successfully")
    finally:
        mydb.commit()


def email_validation(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(regex, email):
        print("invalid email")
        return False
    else:
        return True


def number_validation(phonenumer):
    if not re.match(r"^(\+98|0)?9\d{9}$", phonenumer):
        print("invalid phone number")
        return False
    else:
        return True


def password_validation(password):
    lc = re.compile("[a-z]+")
    lowercase = lc.findall(password)

    uc = re.compile("[A-Z]+")
    uppercase = uc.findall(password)

    cn = re.compile("[0-9]+")
    number = cn.findall(password)

    if len(lowercase) == 0 or len(uppercase) == 0 or len(password) < 6 or len(number) == 0:
        print("invalid password")
        return False
    else:
        return True


def general_check(name, phone, username, password, email):
    check = True
    if name == "":
        print("name field is empty")
        check = False
    if phone == "":
        print("phone field is empty")
        check = False
    if username == "":
        print("username field is empty")
        check = False
    if password == "":
        print("password field is empty")
        check = False
    if email == "":
        print("email field is empty")
        check = False
    return check


def get_hashed_password(passw):
    passwd = str.encode(passw)

    hashed = bcrypt.hashpw(passwd, bcrypt.gensalt(10))

    return hashed


def fields_validation(name, phone, username, password, email, address, postal_code, role):
    if general_check(name, phone, username, password, email):

        if username == "admin":
            print("username can not be the word admin")
        else:
            check = True

            if not number_validation(phone):
                check = False

            if not email_validation(email):
                check = False

            if not password_validation(password):
                check = False

            if check:
                data_dict = {
                    "role": role,
                    "full_name": name,
                    "username": username,
                    "password": password,
                    "email": email,
                    "phone_number": phone,
                    "address": address,
                    "postal_code": postal_code,
                }
                insert_database(data_dict, "users")



