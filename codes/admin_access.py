from datetime import datetime
import mysql.connector


def get_orders_list():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT order_id, user_id, order_status, price, ordering_date, updating_date FROM orders")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


def get_users_list():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT user_id, role, full_name, username, email, phone_number, address, postal_code, "
                     "joining_date  FROM users ORDER BY user_id")

    myresult = mycursor.fetchall()

    return myresult


def remove_user(username):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    users_inuse = user_validation()

    res = [True for item in users_inuse if username in item]

    if len(res) != 0:
        print("unable to remove user (user have a not delivered order)")
    else:
        mycursor = mydb.cursor()

        sql = "DELETE FROM users WHERE username = " + "'" + username + "'"

        mycursor.execute(sql)

        if mycursor.rowcount == 0:
            print("username doesn't found")
        else:
            print(mycursor.rowcount, "user removed")

    mydb.commit()


def add_new_admin(full_name, username, password, email, phone_number, address, postal_code):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    joining_date = datetime.now()

    sql = "INSERT INTO users (role, full_name, username, password, email," \
          " phone_number, address, postal_code, joining_date," \
          " updating_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (1, full_name, username, password, email,
           phone_number, address, postal_code, joining_date, joining_date)

    try:
        mycursor.execute(sql, val)
    except mysql.connector.errors.IntegrityError:
        print("username/email already token")
    else:
        print("inserted successfully")
    finally:
        mydb.commit()


def add_category(name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    cursor = mydb.cursor()

    joining_date = datetime.now()

    sql = "INSERT INTO categories (name, creating_time," \
          " updating_date) VALUES (%s, %s, %s)"

    val = (name, joining_date, joining_date)

    try:
        cursor.execute(sql, val)
    except mysql.connector.errors.IntegrityError:
        print("duplicate category name")
    else:
        mydb.commit()
        print(cursor.rowcount, "record inserted to categories")


def category_validation():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT categories.name FROM categories INNER JOIN products ON categories.category_id = "
                     "products.category_id")

    myresult = mycursor.fetchall()

    mydb.commit()

    return myresult


def user_validation():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT users.username FROM orders INNER JOIN users ON orders.user_id = users.user_id AND "
                     "order_status = 0")

    myresult = mycursor.fetchall()

    mydb.commit()

    return myresult


def remove_category(name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    categories_inuse = category_validation()

    res = [True for item in categories_inuse if name in item]

    if len(res) == 0:

        mycursor = mydb.cursor()

        sql = "DELETE FROM categories WHERE name = " + "'" + name + "'"

        mycursor.execute(sql)

        if mycursor.rowcount == 0:
            print("category doesn't found")
        else:
            print(mycursor.rowcount, "category removed")

    else:
        print("unable to remove category (category is inuse)")

    mydb.commit()


def edit_category_name(before, after):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    cursor = mydb.cursor()

    categories_inuse = category_validation()

    res = [True for item in categories_inuse if before in item]

    sql = "UPDATE categories SET name = " + "'" + after + "'" + " WHERE " + "name = " + "'" + before + "'"

    if len(res) == 0:
        cursor.execute(sql)
        if cursor.rowcount == 0:
            print("category doesn't found")
        else:
            print(cursor.rowcount, "category edited")
            mydb.commit()
            edit_date(after, "categories")

    else:
        print("unable to edit category (category is inuse)")

    mydb.commit()


def edit_date(name, table_name):
    import time

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    cursor = mydb.cursor()

    sql = "UPDATE " + table_name + " SET updating_date = " + "'" + str(
        time.strftime('%Y-%m-%d %H:%M:%S')) + "'" + " WHERE " + "name = " + "'" + name + "'"

    cursor.execute(sql)

    mydb.commit()


def create_report(product_name, description):
    product_id = get_product_id(product_name)

    if len(product_id) == 0:
        print("no such product found")

    else:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1457914neg",
            database="sql_store"
        )

        mycursor = mydb.cursor()

        date = datetime.now()

        sql = "INSERT INTO edit_reports (product_id, updating_date, details) VALUES (%s, %s, %s) "

        val = (product_id[0][0], date, description)

        mycursor.execute(sql, val)
        mydb.commit()
        print("one row added to edit_reports table successfully")


def get_category(category_name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT category_id FROM categories WHERE name = " + "'" + category_name + "'")

    myresult = mycursor.fetchall()

    return myresult


def add_product(category_name, name, count, price):
    validation = fields_validation(name, category_name, count, price)
    if validation:
        category_id = get_category(category_name)
        if len(category_id) == 0:
            print("category doesn't exists")
        else:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1457914neg",
                database="sql_store"
            )

            cursor = mydb.cursor()

            joining_date = datetime.now()

            sql = "INSERT INTO products (category_id, name, count, price, adding_date, updating_date)" \
                  " VALUES (%s, %s, %s,%s, %s, %s)"

            val = (category_id[0][0], name, count, price, joining_date, joining_date)

            try:
                cursor.execute(sql, val)
            except mysql.connector.errors.IntegrityError:
                print("product already exist")
            else:
                print(cursor.rowcount, "record inserted to products")
            finally:
                mydb.commit()


def delete_product(name):
    mydb1 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor1 = mydb1.cursor()

    pro_inuse = product_validation()

    res = [True for item in pro_inuse if name in item]

    if len(res) != 0:
        print("unable to delete product (product exists in an order) ")
    else:
        sql = "DELETE FROM products WHERE name = " + "'" + name + "'"
        mycursor1.execute(sql)
        mydb1.commit()
        if mycursor1.rowcount == 0:
            print("no such product found")
        else:
            print(mycursor1.rowcount, "record(s) affected in products")
    mydb1.commit()


def edit_name(new_name, prev_name):
    mydb1 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor1 = mydb1.cursor()

    pro_inuse = product_validation()

    res = [True for item in pro_inuse if prev_name in item]

    if len(res) != 0:
        print("unable to edit product (product exists in an order) ")
    else:
        sql = "UPDATE products SET name = " + "'" + new_name + "'" + \
              " WHERE " + "name = " + "'" + prev_name + "'"
        mycursor1.execute(sql)

        if mycursor1.rowcount == 0:
            print("product doesn't exist")
        else:
            print(mycursor1.rowcount, "record(s) affected in product name")
            mydb1.commit()
            edit_date(new_name, "products")
            create_report(new_name, "product name changed to " + new_name)

    mydb1.commit()


def edit_count(count, prev_name):
    try:
        int(count)
    except ValueError:
        print("invalid input for count")
    else:
        mydb1 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1457914neg",
            database="sql_store"
        )

        mycursor1 = mydb1.cursor()
        sql = "UPDATE products SET count = " + "'" + count + "'" + \
              " WHERE " + "name = " + "'" + prev_name + "'"
        mycursor1.execute(sql)

        if mycursor1.rowcount == 0:
            print("product doesn't exist")
        else:
            print(mycursor1.rowcount, "record(s) affected in product count")
            mydb1.commit()
            edit_date(prev_name, "products")
            create_report(prev_name, "product count changed to " + str(count))

        mydb1.commit()


def edit_price(price, prev_name):
    try:
        int(price)
    except ValueError:
        print("invalid input for price")
    else:
        mydb1 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1457914neg",
            database="sql_store"
        )

        mycursor1 = mydb1.cursor()
        sql = "UPDATE products SET price = " + "'" + price + "'" + \
              " WHERE " + "name = " + "'" + prev_name + "'"
        mycursor1.execute(sql)

        if mycursor1.rowcount == 0:
            print("product doesn't exist")
        else:
            print(mycursor1.rowcount, "record(s) affected in product price")
            mydb1.commit()
            edit_date(prev_name, "products")
            create_report(prev_name, "product price changed to " + str(price))

        mydb1.commit()


def edit_category(category, prev_name):
    mydb1 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb1.cursor()

    category_id = get_category(category)
    if len(category_id) == 0:
        print("category doesn't exists")
    else:
        pro_inuse = product_validation()

        res = [True for item in pro_inuse if prev_name in item]

        if len(res) != 0:
            print("unable to edit product (product exists in an order) ")
        else:
            sql = "UPDATE products SET category_id = " + "'" + str(category_id[0][0]) + "'" + \
                  " WHERE " + "name = " + "'" + prev_name + "'"
            mycursor.execute(sql)
            if mycursor.rowcount == 0:
                print("no such product found")
            else:
                print(mycursor.rowcount, "record(s) affected in product category")
                mydb1.commit()
                edit_date(prev_name, "products")
                create_report(prev_name, "product category_id changed to " + str(category_id[0][0]))

        mydb1.commit()


def product_validation():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT products.name FROM product_order INNER JOIN products ON product_order.product_id = "
                     "products.product_id INNER JOIN orders ON product_order.order_id = orders.order_id AND "
                     "orders.order_status = 0")

    myresult = mycursor.fetchall()

    mydb.commit()

    return myresult


def fields_validation(product, category, count, price):
    check = True
    if product == "":
        print("product field is empty")
        check = False
    if category == "":
        print("category field is empty")
        check = False
    if count == "":
        print("count field is empty")
        check = False
    if price == "":
        print("price field is empty")
        check = False

    try:
        int(count)
    except ValueError:
        print("count field is not a number")
        check = False

    try:
        int(price)
    except ValueError:
        print("price field is not a number")
        check = False

    return check


def get_product_id(name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT product_id FROM products WHERE name = " + "'" + name + "'")

    myresult = mycursor.fetchall()

    mydb.commit()

    return myresult
