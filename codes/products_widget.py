import pickle

import mysql.connector
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QHBoxLayout)
from PyQt5.QtWidgets import (
    QLabel,
    QWidget,
)
from PyQt5.QtWidgets import (QPushButton)



class Product:
    def __init__(self, name, category, count, price):
        self.name = name
        self.category = category
        self.count = count
        self.price = price

    def __str__(self):
        return self.name + " " + str(self.category) + " " + str(self.count) + " " + str(self.price)


cur_wishlist = []


def get_products():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM products"

    mycursor.execute(sql)

    return_list = mycursor.fetchall()

    return return_list


def get_category(category_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    sql = "SELECT name FROM categories WHERE category_id ='" + str(category_id) + "'"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return myresult[0][0]


def get_category_(category):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    sql = "SELECT name FROM categories WHERE name ='" + str(category) + "'"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    return myresult

def add_to_wishlist(product, label):
    index = get_index(cur_wishlist, product.name)

    if int(label) >= 0:
        category_id = get_category_(product.category)

        if len(category_id) != 0:
            if index == -1:
                new_product = Product(product.name, str(category_id[0][0]), "1", str(product.price))
                cur_wishlist.append(new_product)
            else:
                p_count = int(cur_wishlist[index].count) + 1
                cur_wishlist[index].count = str(p_count)
        else:
            print("category not found")
    else:
        print("not enough inventory")


def save_wishlist_to_file():
    file = open("wishlist.b", "wb")
    pickle.dump(cur_wishlist, file)
    print("wishlist saved")
    file.close()


def object_list(prev_list):
    # name , category_id, count , price
    new_list = []

    for x in range(len(prev_list)):
        category = get_category(prev_list[x][1])
        product = Product(prev_list[x][2], category, prev_list[x][3], prev_list[x][4])
        new_list.append(product)

    return new_list


def sort_list(order, li):
    if order == "name":
        li.sort(key=lambda y: y.name)
    elif order == "category":
        li.sort(key=lambda y: y.category)
    elif order == "price":
        li.sort(key=lambda y: y.price)
    elif order == "count":
        li.sort(key=lambda y: y.count)

    return li


def set_count_label(label):
    count_int = int(label)

    if count_int - 1 >= 0:
        count_int -= 1
        return str(count_int)
    else:
        show_details()
        return "0"


def get_index(wishlist, name):
    return next((i for i, item in enumerate(wishlist) if item.name == name), -1)


def show_details():
    dlg = CustomDialog()
    dlg.exec()


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("warning!")
        self.setGeometry(100, 50, 200, 200)
        self.setStyleSheet("background-color : #4F6367")

        message = QLabel()
        message.setText("Inventory of this product is not enough")
        message.setStyleSheet("color: #FE5F55;"
                              "font-weight: bold;"
                              "display:inline-block")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        message.setFont(font)

        win = self.frameGeometry()
        pos = QDesktopWidget().availableGeometry().center()
        win.moveCenter(pos)
        self.move(win.topLeft())

        self.layout = QVBoxLayout()
        self.layout.addWidget(message)
        self.setLayout(self.layout)


class ProWidget(QWidget):

    def __init__(self, name, category, price, count):
        super(ProWidget, self).__init__()

        self.name = name
        self.category = category
        self.price = price
        self.count = count

        self.name_label = QLabel(self.name)
        self.name_label.setStyleSheet("color: #101111;"
                                      "font-weight: bold;"
                                      "display:inline-block")

        self.category_label = QLabel(self.category)
        self.category_label.setStyleSheet("color: #101111;"
                                          "font-weight: bold;"
                                          "display:inline-block")

        self.price_label = QLabel(self.price)
        self.price_label.setStyleSheet("color: #101111;"
                                       "font-weight: bold;"
                                       "display:inline-block")

        self.count_label = QLabel(self.count)
        self.count_label.setStyleSheet("color: #101111;"
                                       "font-weight: bold;"
                                       "display:inline-block")

        self.space = QLabel(" ")
        self.space.setStyleSheet("color: #101111;"
                                 "font-weight: bold;"
                                 "display:inline-block")

        self.add_product = QPushButton("add")
        self.add_product.setStyleSheet("background-color:#FE5F55;"
                                       "border:1px solid #FE5F55;"
                                       "display:inline-block;"
                                       "color:#EEF5DB;"
                                       "padding:2px 3px;"
                                       "font-weight: bold;")
        self.add_product.clicked.connect(lambda: self.count_label.setText(set_count_label(self.count_label.text())))
        self.add_product.clicked.connect(lambda: add_to_wishlist(Product(self.name, self.category,
                                                                         self.count, self.price),
                                                                 self.count_label.text()))

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.name_label)
        self.hbox.addWidget(self.category_label)
        self.hbox.addWidget(self.price_label)
        self.hbox.addWidget(self.count_label)
        if self.name == "name":
            self.hbox.addWidget(self.space)
        else:
            self.hbox.addWidget(self.add_product)

        self.setLayout(self.hbox)
