from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
import mysql.connector
import datetime


class Order:
    def __init__(self, order_id, username, order_status, total_price, ordering_date, updating_date):
        self.ts = '2013-01-12 15:27:43'
        self.f = '%Y-%m-%d %H:%M:%S'

        datetime.datetime.strptime(self.ts, self.f)
        datetime.datetime(2013, 1, 12, 15, 27, 43)

        self.order_id = order_id
        self.username = username
        self.order_status = order_status
        self.total_price = total_price
        self.ordering_date = ordering_date.strftime(self.f)
        self.updating_date = updating_date.strftime(self.f)

    def __str__(self):

        return str(self.order_id) + " " + self.username + \
               " " + str(self.order_status) + " " + str(self.total_price) + \
               " " + self.ordering_date.strftime(self.f) + " " + self.updating_date.strftime(self.f)


all_orders = []


def get_all_orders():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    cursor = mydb.cursor()

    sql = "SELECT orders.order_id, users.username, orders.order_status, orders.price, orders.ordering_date, " \
          "orders.updating_date FROM orders INNER JOIN users ON orders.user_id = users.user_id; "

    cursor.execute(sql)
    myresult = cursor.fetchall()

    mydb.commit()

    return myresult


def object_list(prev_list):
    new_list = []

    for ord in prev_list:
        order = Order(ord[0], ord[1], ord[2], ord[3], ord[4], ord[5])
        new_list.append(order)

    return new_list


class AllOrdersWidget(QWidget):

    def __init__(self, order_id, username, order_status, total_price, ordering_date, updating_date):
        super(AllOrdersWidget, self).__init__()

        self.order_id = order_id
        self.username = username
        self.order_status = order_status
        self.total_price = total_price
        self.ordering_date = ordering_date
        self.updating_date = updating_date

        self.order_id_label = QLabel(self.order_id)
        self.order_id_label.setStyleSheet("color: #101111;"
                                          "font-weight: bold;"
                                          "display:inline-block")

        self.username_label = QLabel(self.username)
        self.username_label.setStyleSheet("color: #101111;"
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

        self.space1 = QLabel(" ")
        self.space1.setStyleSheet("color: #101111;"
                                  "font-weight: bold;"
                                  "display:inline-block")

        self.space2 = QLabel(" ")
        self.space2.setStyleSheet("color: #101111;"
                                  "font-weight: bold;"
                                  "display:inline-block")

        self.ordering_date_label = QLabel(self.ordering_date)
        self.ordering_date_label.setStyleSheet("color: #101111;"
                                               "font-weight: bold;"
                                               "display:inline-block")

        self.updating_date_label = QLabel(self.updating_date)
        self.updating_date_label.setStyleSheet("color: #101111;"
                                               "font-weight: bold;"
                                               "display:inline-block")

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.order_id_label)
        self.hbox.addWidget(self.username_label)
        self.hbox.addWidget(self.order_status_label)
        self.hbox.addWidget(self.total_price_label)
        self.hbox.addWidget(self.ordering_date_label)
        self.hbox.addWidget(self.updating_date_label)



        self.setLayout(self.hbox)

