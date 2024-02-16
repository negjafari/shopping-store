import datetime

import mysql.connector
from PyQt5.QtWidgets import QDialog, QPushButton
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, \
    QTableWidgetItem, QDesktopWidget, QTableWidget


class CustomDialog(QDialog):
    def __init__(self, order_id):
        super().__init__()

        self.setWindowTitle("ORDER DETAILS")
        self.setGeometry(100, 100, 500, 300)

        list = get_orders_detail(order_id)

        table = QTableWidget(self)
        table.setColumnCount(6)
        table.setRowCount(len(list))
        table.setMinimumWidth(1300)
        table.setMinimumHeight(1000)

        table.setHorizontalHeaderLabels(["order_id", "product_name", "product_price", "count",
                                         "total_price", "order_status", "insert_time"])

        for i in range(len(list)):
            for j in range(6):
                if j == 5:
                    status = str(list[i][j])
                    if status == "0":
                        table.setItem(i, j, QTableWidgetItem("preparing"))
                    elif status == "-1":
                        table.setItem(i, j, QTableWidgetItem("canceled"))
                    elif status == "1":
                        table.setItem(i, j, QTableWidgetItem("received"))
                else:
                    table.setItem(i, j, QTableWidgetItem(str(list[i][j])))

        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        table.show()

        win = self.frameGeometry()
        pos = QDesktopWidget().availableGeometry().center()
        win.moveCenter(pos)
        self.move(win.topLeft())


        self.layout = QVBoxLayout()
        self.setLayout(self.layout)


class Order:
    def __init__(self, order_id, order_status, total_price, ordering_date):
        self.ts = '2013-01-12 15:27:43'
        self.f = '%Y-%m-%d %H:%M:%S'

        datetime.datetime.strptime(self.ts, self.f)
        datetime.datetime(2013, 1, 12, 15, 27, 43)

        self.order_id = order_id
        self.order_status = order_status
        self.total_price = total_price
        self.ordering_date = ordering_date.strftime(self.f)

    def __str__(self):
        return str(self.order_id) + \
               " " + str(self.order_status) + " " + str(self.total_price) + \
               " " + self.ordering_date


my_orders = []


def get_my_orders(user_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    cursor = mydb.cursor()

    sql = "SELECT * FROM orders WHERE user_id = " + user_id

    cursor.execute(sql)
    myresult = cursor.fetchall()

    mydb.commit()


    return myresult


def object_list(prev_list):
    new_list = []

    for ord in prev_list:
        order = Order(ord[0], ord[2], ord[3], ord[4])
        new_list.append(order)

    return new_list


def get_orders_detail(order_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    cursor = mydb.cursor()

    sql = "SELECT product_order.order_id, products.name,products.price, product_order.count, " \
          "product_order.unit_price, orders.order_status ,product_order.insert_time FROM product_order INNER JOIN " \
          "products ON product_order.product_id = products.product_id INNER JOIN orders ON product_order.order_id = " \
          "orders.order_id AND product_order.order_id = " + order_id

    cursor.execute(sql)
    myresult = cursor.fetchall()

    mydb.commit()

    return myresult


def show_details(order_id):
    dlg = CustomDialog(str(order_id))
    dlg.setWindowTitle("ORDER DETAILS")
    dlg.exec()


def cancel_order(order_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    sql = "UPDATE orders SET order_status = -1 WHERE order_id = " + order_id + " AND order_status = 0 "

    mycursor.execute(sql)

    mydb.commit()

    if mycursor.rowcount == 0:
        print("The sent order cannot be deleted")
    else:
        print(mycursor.rowcount, "orders canceled")
        update_canceled_products_inventory(order_id)


def canceled_products(order_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    sql = "SELECT product_id FROM product_order WHERE order_id = " + order_id

    mycursor.execute(sql)

    res = mycursor.fetchall()

    mydb.commit()

    return res


def update_canceled_products_inventory(order_id):
    can_products = canceled_products(str(order_id))
    for pro in can_products:
        update_database(str(order_id), str(pro[0]))


def update_database(order_id, product_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    sql = "UPDATE products JOIN (SELECT * FROM products) " \
          "temp_p ON products.product_id = temp_p.product_id " \
          "SET products.count = temp_p.count + " \
          "(SELECT count FROM product_order WHERE product_id = " + product_id \
          + " AND order_id = " + order_id + ") WHERE products.product_id = " + product_id

    mycursor.execute(sql)

    print(mycursor.rowcount, "record(s) updated in database")
    mydb.commit()


class MyOrdersWidget(QWidget):

    def __init__(self, order_id, order_status, total_price, ordering_date):
        super(MyOrdersWidget, self).__init__()

        self.order_id = order_id
        self.order_status = order_status
        self.total_price = total_price
        self.ordering_date = ordering_date

        self.order_id_label = QLabel(self.order_id)
        self.order_id_label.setStyleSheet("color: #101111;"
                                          "font-weight: bold;"
                                          "display:inline-block")

        self.order_status_label = QLabel(self.order_status)
        self.order_status_label.setStyleSheet("color: #101111;"
                                              "font-weight: bold;"
                                              "display:inline-block")

        self.total_price_label = QLabel(self.total_price)
        self.total_price_label.setStyleSheet("color: #101111;"
                                             "font-weight: bold;"
                                             "display:inline-block")

        self.ordering_date_label = QLabel(self.ordering_date)
        self.ordering_date_label.setStyleSheet("color: #101111;"
                                               "font-weight: bold;"
                                               "display:inline-block")

        self.space1 = QLabel(" ")
        self.space1.setStyleSheet("color: #101111;"
                                  "font-weight: bold;"
                                  "display:inline-block")

        self.space2 = QLabel(" ")
        self.space2.setStyleSheet("color: #101111;"
                                  "font-weight: bold;"
                                  "display:inline-block")

        self.details_btn = QPushButton("details")
        self.details_btn.setStyleSheet("background-color:#FE5F55;"
                                       "border:1px solid #FE5F55;"
                                       "display:inline-block;"
                                       "color:#EEF5DB;"
                                       "padding:2px 3px;"
                                       "font-weight: bold;")
        self.details_btn.clicked.connect(lambda: show_details(self.order_id))

        self.canecl_btn = QPushButton("cancel order")
        self.canecl_btn.setStyleSheet("background-color:#FE5F55;"
                                      "border:1px solid #FE5F55;"
                                      "display:inline-block;"
                                      "color:#EEF5DB;"
                                      "padding:2px 3px;"
                                      "font-weight: bold;")
        self.canecl_btn.clicked.connect(lambda: cancel_order(str(self.order_id)))

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.order_id_label)
        self.hbox.addWidget(self.order_status_label)
        self.hbox.addWidget(self.total_price_label)
        self.hbox.addWidget(self.ordering_date_label)

        if self.order_id == "order_id":
            self.hbox.addWidget(self.space1)
            self.hbox.addWidget(self.space2)

        else:
            self.hbox.addWidget(self.details_btn)
            self.hbox.addWidget(self.canecl_btn)

        self.setLayout(self.hbox)
