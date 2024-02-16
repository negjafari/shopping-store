import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QGridLayout, QHBoxLayout)
from PyQt5.QtWidgets import (
    QLabel,
)
from PyQt5.QtWidgets import (
    QVBoxLayout,
)
from PyQt5 import QtGui
import pickle


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


def get_new_products_widget(product_list):
    product = QVBoxLayout()

    product_name = QLabel()
    product_name.setText(product_list.name)

    product_category = QLabel()
    product_category.setText(product_list.category)

    product_count = QLabel()
    product_count.setText(str(product_list.count))

    product_price = QLabel()
    product_price.setText(str(product_list.price))

    add_product = QPushButton()
    add_product.setText("add")
    add_product.setStyleSheet("background-color:#FE5F55;"
                              "border-radius:10px;"
                              "border:1px solid #FE5F55;"
                              "display:inline-block;"
                              "color:#EEF5DB;"
                              "padding:2px 3px;")
    add_product.clicked.connect(lambda: product_count.setText(set_count_label(product_count.text())))
    add_product.clicked.connect(lambda: add_to_wishlist(Product(product_list.name, product_list.category,
                                                                product_list.count, product_list.price),
                                                        product_count.text()))


    product.addWidget(product_name)
    product.addWidget(product_category)
    product.addWidget(product_price)
    product.addWidget(product_count)
    product.addWidget(add_product)
    product.addSpacing(5)

    return product


def show_products_list():
    groupBox = QGroupBox("Products List")

    product_list = get_products()
    obj_product_list = object_list(product_list)

    name_btn = QPushButton('name')
    name_btn.setStyleSheet("background-color:#FE5F55;"
                           "border-radius:10px;"
                           "border:1px solid #FE5F55;"
                           "display:inline-block;"
                           "color:#EEF5DB;"
                           "padding:2px 3px;")
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(True)
    name_btn.setFont(font)
    # name_btn.clicked.connect(lambda: test(obj_product_list))

    category_btn = QPushButton('category')
    category_btn.setStyleSheet("background-color:#FE5F55;"
                               "border-radius:10px;"
                               "border:1px solid #FE5F55;"
                               "display:inline-block;"
                               "color:#EEF5DB;"
                               "padding:2px 3px;")
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(True)
    category_btn.setFont(font)

    price_btn = QPushButton('price')
    price_btn.setStyleSheet("background-color:#FE5F55;"
                            "border-radius:10px;"
                            "border:1px solid #FE5F55;"
                            "display:inline-block;"
                            "color:#EEF5DB;"
                            "padding:2px 3px;")
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(True)
    price_btn.setFont(font)

    count_btn = QPushButton('count')
    count_btn.setStyleSheet("background-color:#FE5F55;"
                            "border-radius:10px;"
                            "border:1px solid #FE5F55;"
                            "display:inline-block;"
                            "color:#EEF5DB;"
                            "padding:2px 3px;")
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(True)
    count_btn.setFont(font)

    layout = QGridLayout()

    sorted_list = sort_list("name", obj_product_list)

    for i in range(0, len(sorted_list)):
        container = QHBoxLayout()
        container.addLayout(get_new_products_widget(sorted_list[i]))

        layout.addLayout(container, i + 5, 0)

    groupBox.setLayout(layout)

    scroll = QScrollArea()
    scroll.setWidget(groupBox)
    scroll.setWidgetResizable(True)
    scroll.setFixedHeight(300)
    main_layout = QVBoxLayout()

    submit_btn = QPushButton('submit')
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
    submit_btn.clicked.connect(lambda: save_wishlist_to_file())

    main_layout.addWidget(name_btn)
    main_layout.addWidget(category_btn)
    main_layout.addWidget(price_btn)
    main_layout.addWidget(count_btn)
    main_layout.addWidget(scroll)
    main_layout.addWidget(submit_btn)

    return main_layout


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

    # print(myresult)

    return myresult[0][0]


def add_to_wishlist(product, label):
    index = get_index(cur_wishlist, product.name)

    if int(label) >= 0:
        category_id = get_category(product.category)

        if len(category_id) != 0:
            if index == -1:
                new_product = Product(product.name, str(category_id[0][0]), "1", str(product.price))
                cur_wishlist.append(new_product)
            else:
                p_count = int(cur_wishlist[index].count) + 1
                cur_wishlist[index].count = str(p_count)
                print(cur_wishlist[index])
        else:
            print("category not found")
    else:
        print("not enough in main")


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
        print("not enough product")
        return "0"


def get_index(wishlist, name):
    return next((i for i, item in enumerate(wishlist) if item.name == name), -1)

