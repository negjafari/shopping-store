from PyQt5.QtWidgets import (QGridLayout, QHBoxLayout)
import pickle
from datetime import datetime
from enum import Enum

import mysql
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QGridLayout, QHBoxLayout)
from PyQt5.QtWidgets import (
    QLabel,
)
from PyQt5.QtWidgets import (
    QVBoxLayout,
)

from codes.products import get_index
from codes.products_widget import Product


class Orders(Enum):
    PREPARING = 0
    CANCELED = -1
    RECEIVED = 1


class User:
    def __init__(self):
        pass

    def set_userid(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id


class WishList:
    def __init__(self):
        self.wishlist = []

    def load_list(self, cur_list):
        self.wishlist = cur_list


user = User()
current_list = WishList()


def get_new_products_widget(product_list):
    product = QVBoxLayout()

    product_name = QLabel()
    product_name.setText("name : " + product_list.name)

    product_category = QLabel()
    product_category.setText("category : " + product_list.category)

    product_count = QLabel()
    c = str(product_list.count)
    product_count.setText("count : " + c)

    product_price = QLabel()
    p = str(product_list.price)
    product_price.setText("price : " + p)

    remove_product = QPushButton()
    remove_product.setText("remove")
    remove_product.setStyleSheet("background-color:#FE5F55;"
                                 "border-radius:10px;"
                                 "border:1px solid #FE5F55;"
                                 "display:inline-block;"
                                 "color:#EEF5DB;"
                                 "padding:2px 3px;")
    remove_product.clicked.connect(lambda: remove_selected_product(product_list.name))

    product.addWidget(product_name)
    product.addWidget(product_category)
    product.addWidget(product_price)
    product.addWidget(product_count)
    product.addWidget(remove_product)
    product.addSpacing(5)

    return product


def show_wishlist():
    groupBox = QGroupBox("My Wishlist")

    pro_list_changes = check_current_prices()

    layout = QGridLayout()

    for i in range(0, len(pro_list_changes)):
        container = QHBoxLayout()
        try:
            container.addLayout(get_new_products_widget(pro_list_changes[i]))
        except AttributeError:
            print(len(pro_list_changes))

        # container.addSpacing(10)

        layout.addLayout(container, i, 0)

    layout.setHorizontalSpacing(5)
    layout.setVerticalSpacing(1)

    groupBox.setLayout(layout)

    remove_list_btn = QPushButton('remove all products')
    remove_list_btn.setStyleSheet("background-color:#FE5F55;"
                                  "border-radius:10px;"
                                  "border:1px solid #FE5F55;"
                                  "display:inline-block;"
                                  "color:#EEF5DB;"
                                  "padding:2px 3px;")
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(True)
    remove_list_btn.setFont(font)
    remove_list_btn.clicked.connect(lambda: remove_all_products())

    submit_btn = QPushButton('order')
    submit_btn.setStyleSheet("background-color:#FE5F55;"
                             "border-radius:10px;"
                             "border:1px solid #FE5F55;"
                             "display:inline-block;"
                             "color:#EEF5DB;"
                             "padding:2px 3px;")
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(True)
    submit_btn.setFont(font)
    submit_btn.clicked.connect(lambda: submit_order())

    scroll = QScrollArea()
    scroll.setWidget(groupBox)
    scroll.setWidgetResizable(True)
    scroll.setFixedHeight(300)
    main_layout = QVBoxLayout()
    main_layout.addWidget(remove_list_btn)
    main_layout.addWidget(scroll)
    main_layout.addWidget(submit_btn)

    return main_layout


def load_wishlist():
    try:
        file_pi2 = open('wishlist.b', 'rb')
        object_pi2 = pickle.load(file_pi2)
        current_list.load_list(object_pi2)
        return object_pi2
    except IOError:
        current_list.load_list([])
        return []


def remove_all_products():
    # open("wishlist.b", "wb").close()
    empty_list = []
    # Open the pickle file in 'wb' so that you can write and dump the empty variable
    openfile = open('wishlist.b', 'wb')
    pickle.dump(empty_list, openfile)
    openfile.close()
    print("file data cleared")


def remove_selected_product(name):
    f1 = open("wishlist.b", "rb")

    li = []

    while True:
        try:
            li = pickle.load(f1)
            ind = get_index(li, name)
            prev_count = int(li[ind].count)
            if prev_count > 0:
                prev_count -= 1
                li[ind].count = str(prev_count)
            else:
                li[ind].count = "0"

        except EOFError:
            print("Completed Updating details")
            break

    f1.close()

    f2 = open("wishlist.b", "wb")
    pickle.dump(li, f2)
    f2.close()


def read_file():
    f = open("wishlist.b", 'rb')
    while True:
        try:
            wishlist = pickle.load(f)

            for i in wishlist:
                print(i)

        except EOFError:
            print("read file completely")
            break
    f.close()


def create_order_table(table_name, user_id, price, order_status):
    # order status : 0 => preparing , -1 => canceled , 1 => received

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    cursor = mydb.cursor()

    joining_date = datetime.now()

    sql = "INSERT INTO " + table_name + " (user_id, order_status, price, ordering_date, updating_date) " \
                                        "VALUES (%s, %s, %s, %s, %s)"

    val = (user_id, order_status, price, joining_date, joining_date)

    cursor.execute(sql, val)
    mydb.commit()
    print("successfully inserted to orders table")
    return cursor.lastrowid


def create_product_orders_table(table_name, order_id, pro):
    # id, order_id, product_id, count, unit_price, insert_time, update_time

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    cursor = mydb.cursor()

    joining_date = datetime.now()
    product_id = get_product_id(pro.name)
    int_count = int(pro.count)

    price = int(pro.price) * int_count

    sql = "INSERT INTO " + table_name + " (order_id, product_id, count, unit_price, insert_time, updating_date) " \
                                        "VALUES (%s, %s, %s, %s, %s, %s)"

    val = (order_id, product_id[0][0], pro.count, price, joining_date, joining_date)

    cursor.execute(sql, val)
    mydb.commit()
    print("successfully inserted to product_order table")


def count_total_price(products_list):
    price = 0
    for pro in products_list:
        int_price = int(pro.price)
        int_count = int(pro.count)
        price += int_price * int_count

    return price


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


def decrease_count(name, count):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    sql = "UPDATE products SET count = " + count + " WHERE name = " + name

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")


def submit_order():
    if check_current_inventory(current_list.wishlist):
        print("Inventory is not enough")
    else:
        order_status = Orders.PREPARING
        total_price = count_total_price(current_list.wishlist)

        from codes.login import load_current_user_data
        loaded_user = load_current_user_data().user_id

        order_id = create_order_table("orders", int(loaded_user), total_price, order_status.value)

        for pro in current_list.wishlist:
            count = int(pro.count)

            if count > 0:
                create_product_orders_table("product_order", int(order_id), pro)

        for prod in current_list.wishlist:
            count = int(prod.count)

            if count > 0:
                product_id = get_product_id(prod.name)
                update_database(str(product_id[0][0]), str(order_id))

        remove_all_products()


def update_database(product_id, order_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    cursor = mydb.cursor()

    sql = "UPDATE products JOIN (SELECT * FROM products)" \
          " temp_p ON products.product_id = temp_p.product_id " \
          "SET products.count = temp_p.count - " \
          "(SELECT count FROM product_order WHERE product_id = " + product_id \
          + " AND order_id = " + order_id + " ) WHERE products.product_id = " + product_id

    cursor.execute(sql)
    mydb.commit()
    print(cursor.rowcount, "record(s) affected in update database")


def get_current_inventory(name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    cursor = mydb.cursor()

    cursor.execute("SELECT count FROM products WHERE name = " + "'" + name + "'")

    myresult = cursor.fetchall()

    mydb.commit()

    return myresult


def current_prices(product_name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    cursor = mydb.cursor()

    cursor.execute("SELECT price FROM products WHERE name = " + "'" + product_name + "'")

    myresult = cursor.fetchall()

    mydb.commit()

    return myresult


# return true if inventory is not enough
def check_current_inventory(wishlist):
    for item in wishlist:
        p_name = item.name
        p_count = int(item.count)
        cur_inventory = get_current_inventory(p_name)
        c_count = cur_inventory[0][0]

        return p_count > c_count


def check_current_prices():
    wishlist = load_wishlist()
    new_list = []

    for item in wishlist:
        name = item.name
        cur_price = current_prices(name)[0][0]
        new_pro = Product(name, item.category, item.count, cur_price)
        new_list.append(new_pro)

    return new_list


