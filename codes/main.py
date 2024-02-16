import sys

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
)

from codes.admin_access import add_category
from codes.admin_access import add_product
from codes.admin_access import remove_category
from codes.admin_access import delete_product
from codes.admin_access import remove_user
from codes.admin_access import edit_category_name
from codes.admin_access import edit_category
from codes.admin_access import edit_count
from codes.admin_access import edit_name
from codes.admin_access import edit_price
from codes.login import login_validation
from codes.signup import fields_validation
from codes.admin_access import get_users_list
from codes.wishlist import show_wishlist
from codes.reports import get_inventory_report
from codes.reports import get_total_sales
from codes.reports import get_edit_reports
from codes.products_widget import ProWidget
from codes.all_orders_widget import AllOrdersWidget
from codes.my_orders_widget import MyOrdersWidget
from codes.login import save_current_user_data
from codes.login import load_current_user_data
from enum import Enum


class Roles(Enum):
    ADMIN = 1
    USER = 2


class SignupWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("SIGN UP")
        self.setGeometry(100, 100, 300, 600)
        self.uiComponents()
        self.setStyleSheet("background-color : #4F6367")

    def uiComponents(self):
        self.title = QLabel(self)
        self.title.setText("SIGNUP")
        self.title.setGeometry(20, 30, 260, 60)
        self.title.setStyleSheet("color : #FE5F55")
        self.title.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(25)
        self.title.setFont(font)

        self.name_edittext = QLineEdit(self)
        self.name_edittext.setText("name")
        self.name_edittext.setAlignment(Qt.AlignCenter)
        self.name_edittext.setStyleSheet("background-color:#B8D8D8;"
                                         "border-radius:10px;"
                                         "border:1px solid #B8D8D8;"
                                         "display:inline-block;"
                                         "color:#000;"
                                         "padding:10px 10px;")
        self.name_edittext.move(50, 110)
        self.name_edittext.resize(200, 36)

        self.phone_edittext = QLineEdit(self)
        self.phone_edittext.setText("phone number")
        self.phone_edittext.setAlignment(Qt.AlignCenter)
        self.phone_edittext.setStyleSheet("background-color:#B8D8D8;"
                                          "border-radius:10px;"
                                          "border:1px solid #B8D8D8;"
                                          "display:inline-block;"
                                          "color:#000;"
                                          "padding:10px 10px;")
        self.phone_edittext.move(50, 150)
        self.phone_edittext.resize(200, 36)

        self.email_edittext = QLineEdit(self)
        self.email_edittext.setText("email")
        self.email_edittext.setAlignment(Qt.AlignCenter)
        self.email_edittext.setStyleSheet("background-color:#B8D8D8;"
                                          "border-radius:10px;"
                                          "border:1px solid #B8D8D8;"
                                          "display:inline-block;"
                                          "color:#000;"
                                          "padding:10px 10px;")
        self.email_edittext.move(50, 190)
        self.email_edittext.resize(200, 36)

        self.username_edittext = QLineEdit(self)
        self.username_edittext.setText("username")
        self.username_edittext.setAlignment(Qt.AlignCenter)
        self.username_edittext.setStyleSheet("background-color:#B8D8D8;"
                                             "border-radius:10px;"
                                             "border:1px solid #B8D8D8;"
                                             "display:inline-block;"
                                             "color:#000;"
                                             "padding:10px 10px;")
        self.username_edittext.move(50, 230)
        self.username_edittext.resize(200, 36)

        self.password_edittext = QLineEdit(self)
        self.password_edittext.setText("password")
        self.password_edittext.setAlignment(Qt.AlignCenter)
        self.password_edittext.setStyleSheet("background-color:#B8D8D8;"
                                             "border-radius:10px;"
                                             "border:1px solid #B8D8D8;"
                                             "display:inline-block;"
                                             "color:#000;"
                                             "padding:10px 10px;")
        self.password_edittext.move(50, 270)
        self.password_edittext.resize(200, 36)

        self.address_edittext = QLineEdit(self)
        self.address_edittext.setText("address")
        self.address_edittext.setAlignment(Qt.AlignCenter)
        self.address_edittext.setStyleSheet("background-color:#B8D8D8;"
                                            "border-radius:10px;"
                                            "border:1px solid #B8D8D8;"
                                            "display:inline-block;"
                                            "color:#000;"
                                            "padding:10px 10px;")
        self.address_edittext.move(50, 310)
        self.address_edittext.resize(200, 36)

        self.postal_code_edittext = QLineEdit(self)
        self.postal_code_edittext.setText("postal code")
        self.postal_code_edittext.setAlignment(Qt.AlignCenter)
        self.postal_code_edittext.setStyleSheet("background-color:#B8D8D8;"
                                                "border-radius:10px;"
                                                "border:1px solid #B8D8D8;"
                                                "display:inline-block;"
                                                "color:#000;"
                                                "padding:10px 10px;")
        self.postal_code_edittext.move(50, 350)
        self.postal_code_edittext.resize(200, 36)

        self.signup_btn = QPushButton(self)
        self.signup_btn.setText("signup")
        self.signup_btn.clicked.connect(lambda: fields_validation(self.name_edittext.text(),
                                                                  self.phone_edittext.text(),
                                                                  self.username_edittext.text(),
                                                                  self.password_edittext.text(),
                                                                  self.email_edittext.text(),
                                                                  self.address_edittext.text(),
                                                                  self.postal_code_edittext.text(),
                                                                  Roles.USER.value))
        self.signup_btn.setGeometry(50, 430, 200, 50)
        self.signup_btn.setStyleSheet("background-color:#FE5F55;"
                                      "border-radius:10px;"
                                      "border:1px solid #FE5F55;"
                                      "display:inline-block;"
                                      "color:#EEF5DB;"
                                      "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.signup_btn.setFont(font)

        # self.signup = QLabel(self)
        # self.signup.setText("already have an account? login")
        # self.signup.setGeometry(20, 490, 260, 60)
        # self.signup.setStyleSheet("color : #B8D8D8")
        # self.signup.setAlignment(Qt.AlignCenter)
        # font = QtGui.QFont()
        # font.setBold(True)
        # font.setPointSize(8)
        # self.signup.setFont(font)


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("LOGIN")
        self.setGeometry(100, 100, 300, 500)
        self.uiComponents()
        self.setStyleSheet("background-color : #4F6367")
        self.admin_accesses = AdminAccessWindow()
        self.user_accesses = UserAccessesWindow()
        self.selected_role = 0

    def toggle_window(self, window):
        save_current_user_data(self.username_edittext.text())
        if window.isVisible():
            window.hide()

        else:
            window.show()

    def change_selected_role(self, role):
        self.selected_role = role

    def change_window(self, role):

        if role == Roles.ADMIN.value:
            self.toggle_window(self.admin_accesses)
        else:
            self.toggle_window(self.user_accesses)

    def check_change(self, username, password, role):
        check = login_validation(username, password, role)

        if check:
            self.change_window(self.selected_role)

    def uiComponents(self):
        self.title = QLabel(self)
        self.title.setText("LOGIN")
        self.title.setGeometry(20, 30, 260, 60)
        self.title.setStyleSheet("color : #FE5F55")
        self.title.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(25)
        self.title.setFont(font)

        self.username_edittext = QLineEdit(self)
        self.username_edittext.setText("username")
        self.username_edittext.setAlignment(Qt.AlignCenter)
        self.username_edittext.setStyleSheet("background-color:#B8D8D8;"
                                             "border-radius:10px;"
                                             "border:1px solid #B8D8D8;"
                                             "display:inline-block;"
                                             "color:#000;"
                                             "padding:10px 10px;")
        self.username_edittext.move(50, 110)
        self.username_edittext.resize(200, 36)

        self.password_edittext = QLineEdit(self)
        self.password_edittext.setText("password")
        self.password_edittext.setAlignment(Qt.AlignCenter)
        self.password_edittext.setStyleSheet("background-color:#B8D8D8;"
                                             "border-radius:10px;"
                                             "border:1px solid #B8D8D8;"
                                             "display:inline-block;"
                                             "color:#000;"
                                             "padding:10px 10px;")
        self.password_edittext.move(50, 170)
        self.password_edittext.resize(200, 36)

        self.user_login_btn = QPushButton(self)
        self.user_login_btn.setText("login as a user")
        self.user_login_btn.setGeometry(50, 250, 95, 50)
        self.user_login_btn.setStyleSheet("background-color:#FE5F55;"
                                          "border-radius:10px;"
                                          "border:1px solid #FE5F55;"
                                          "display:inline-block;"
                                          "color:#EEF5DB;"
                                          "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.user_login_btn.clicked.connect(lambda: self.change_selected_role(Roles.USER.value))
        self.user_login_btn.setFont(font)

        self.admin_login_btn = QPushButton(self)
        self.admin_login_btn.setText("login as admin")
        self.admin_login_btn.setGeometry(150, 250, 95, 50)
        self.admin_login_btn.setStyleSheet("background-color:#FE5F55;"
                                           "border-radius:10px;"
                                           "border:1px solid #FE5F55;"
                                           "display:inline-block;"
                                           "color:#EEF5DB;"
                                           "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.admin_login_btn.clicked.connect(lambda: self.change_selected_role(Roles.ADMIN.value))
        self.admin_login_btn.setFont(font)

        # self.signup_btn = QPushButton(self)
        # self.signup_btn.setText("don't have account? signup")
        # self.signup_btn.setGeometry(20, 300, 260, 60)
        # self.signup_btn.setStyleSheet("background-color:#4F6367;"
        #                               "border:0px solid #FE5F55;"
        #                               "color:#EEF5DB;"
        #                               "padding:2px 3px;")
        # font = QtGui.QFont()
        # font.setPointSize(8)
        # self.signup_btn.setFont(font)

        self.login_btn = QPushButton(self)
        self.login_btn.setText("login")
        self.login_btn.clicked.connect(lambda: self.check_change(self.username_edittext.text(),
                                                                 self.password_edittext.text(),
                                                                 self.selected_role))
        self.login_btn.setGeometry(50, 430, 200, 50)
        self.login_btn.setStyleSheet("background-color:#FE5F55;"
                                     "border-radius:10px;"
                                     "border:1px solid #FE5F55;"
                                     "display:inline-block;"
                                     "color:#EEF5DB;"
                                     "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.login_btn.setFont(font)


class AdminAccessWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ADMIN ACCESSES")
        self.setGeometry(100, 50, 300, 600)
        self.UiComponents()
        self.setStyleSheet("background-color : #4F6367")
        self.add_admin_win = NewAdminInfo()
        self.users_list_win = UsersListWindow()
        self.delete_user_win = DeleteUserWindow()
        self.add_category_win = ChangeCategoriesWindow()
        self.add_product_win = AddProductWindow()
        self.delete_product_win = DeleteProductWindow()
        self.edit_product_win = EditProductWindow()
        self.reports_win = ReportsWindow()
        self.all_orders_win = AllOrdersWindow()

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()

    def admin_check(self):
        from codes.login import load_current_user_data
        username = load_current_user_data().username
        if username == "admin":
            self.toggle_window(self.add_admin_win)
        else:
            print("only one admin can add new admins")

    def UiComponents(self):
        self.title = QLabel(self)
        self.title.setText("ADMIN ACCESSES")
        self.title.setGeometry(20, 5, 260, 60)
        self.title.setStyleSheet("color : #FE5F55")
        self.title.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.title.setFont(font)

        self.add_admin_btn = QPushButton(self)
        self.add_admin_btn.setText("add admin")
        self.add_admin_btn.setGeometry(90, 70, 120, 40)
        self.add_admin_btn.setStyleSheet("background-color:#FE5F55;"
                                         "border-radius:10px;"
                                         "border:1px solid #FE5F55;"
                                         "display:inline-block;"
                                         "color:#EEF5DB;"
                                         "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.add_admin_btn.setFont(font)
        self.add_admin_btn.clicked.connect(lambda: self.admin_check())

        self.users_list_btn = QPushButton(self)
        self.users_list_btn.setText("users list")
        self.users_list_btn.setGeometry(90, 120, 120, 40)
        self.users_list_btn.setStyleSheet("background-color:#FE5F55;"
                                          "border-radius:10px;"
                                          "border:1px solid #FE5F55;"
                                          "display:inline-block;"
                                          "color:#EEF5DB;"
                                          "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.users_list_btn.setFont(font)
        self.users_list_btn.clicked.connect(lambda checked: self.toggle_window(self.users_list_win))

        self.delete_users_btn = QPushButton(self)
        self.delete_users_btn.setText("remove user")
        self.delete_users_btn.setGeometry(90, 170, 120, 40)
        self.delete_users_btn.setStyleSheet("background-color:#FE5F55;"
                                            "border-radius:10px;"
                                            "border:1px solid #FE5F55;"
                                            "display:inline-block;"
                                            "color:#EEF5DB;"
                                            "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.delete_users_btn.setFont(font)
        self.delete_users_btn.clicked.connect(lambda checked: self.toggle_window(self.delete_user_win))

        self.add_product_btn = QPushButton(self)
        self.add_product_btn.setText("add product")
        self.add_product_btn.setGeometry(90, 220, 120, 40)
        self.add_product_btn.setStyleSheet("background-color:#FE5F55;"
                                           "border-radius:10px;"
                                           "border:1px solid #FE5F55;"
                                           "display:inline-block;"
                                           "color:#EEF5DB;"
                                           "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.add_product_btn.setFont(font)
        self.add_product_btn.clicked.connect(lambda checked: self.toggle_window(self.add_product_win))

        self.edit_product_btn = QPushButton(self)
        self.edit_product_btn.setText("edit product")
        self.edit_product_btn.setGeometry(90, 270, 120, 40)
        self.edit_product_btn.setStyleSheet("background-color:#FE5F55;"
                                            "border-radius:10px;"
                                            "border:1px solid #FE5F55;"
                                            "display:inline-block;"
                                            "color:#EEF5DB;"
                                            "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.edit_product_btn.setFont(font)
        self.edit_product_btn.clicked.connect(lambda checked: self.toggle_window(self.edit_product_win))

        self.delete_product_btn = QPushButton(self)
        self.delete_product_btn.setText("delete product")
        self.delete_product_btn.setGeometry(90, 320, 120, 40)
        self.delete_product_btn.setStyleSheet("background-color:#FE5F55;"
                                              "border-radius:10px;"
                                              "border:1px solid #FE5F55;"
                                              "display:inline-block;"
                                              "color:#EEF5DB;"
                                              "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.delete_product_btn.setFont(font)
        self.delete_product_btn.clicked.connect(lambda checked: self.toggle_window(self.delete_product_win))

        self.orders_list_btn = QPushButton(self)
        self.orders_list_btn.setText("orders list")
        self.orders_list_btn.setGeometry(90, 370, 120, 40)
        self.orders_list_btn.setStyleSheet("background-color:#FE5F55;"
                                           "border-radius:10px;"
                                           "border:1px solid #FE5F55;"
                                           "display:inline-block;"
                                           "color:#EEF5DB;"
                                           "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.orders_list_btn.setFont(font)
        self.orders_list_btn.clicked.connect(lambda checked: self.toggle_window(self.all_orders_win))

        self.category_btn = QPushButton(self)
        self.category_btn.setText("category works")
        self.category_btn.setGeometry(90, 420, 120, 40)
        self.category_btn.setStyleSheet("background-color:#FE5F55;"
                                        "border-radius:10px;"
                                        "border:1px solid #FE5F55;"
                                        "display:inline-block;"
                                        "color:#EEF5DB;"
                                        "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.category_btn.setFont(font)
        self.category_btn.clicked.connect(lambda checked: self.toggle_window(self.add_category_win))

        self.reports_btn = QPushButton(self)
        self.reports_btn.setText("reports")
        self.reports_btn.setGeometry(90, 470, 120, 40)
        self.reports_btn.setStyleSheet("background-color:#FE5F55;"
                                       "border-radius:10px;"
                                       "border:1px solid #FE5F55;"
                                       "display:inline-block;"
                                       "color:#EEF5DB;"
                                       "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.reports_btn.setFont(font)
        self.reports_btn.clicked.connect(lambda checked: self.toggle_window(self.reports_win))


class NewAdminInfo(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("SIGNUP")
        self.setGeometry(100, 100, 300, 600)
        self.uiComponents()
        self.setStyleSheet("background-color : #4F6367")

    def uiComponents(self):
        self.title = QLabel(self)
        self.title.setText("ADMIN SIGNUP")
        self.title.setGeometry(20, 30, 260, 60)
        self.title.setStyleSheet("color : #FE5F55")
        self.title.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(25)
        self.title.setFont(font)

        self.name_edittext = QLineEdit(self)
        self.name_edittext.setText("name")
        self.name_edittext.setAlignment(Qt.AlignCenter)
        self.name_edittext.setStyleSheet("background-color:#B8D8D8;"
                                         "border-radius:10px;"
                                         "border:1px solid #B8D8D8;"
                                         "display:inline-block;"
                                         "color:#000;"
                                         "padding:10px 10px;")
        self.name_edittext.move(50, 110)
        self.name_edittext.resize(200, 36)

        self.phone_edittext = QLineEdit(self)
        self.phone_edittext.setText("phone number")
        self.phone_edittext.setAlignment(Qt.AlignCenter)
        self.phone_edittext.setStyleSheet("background-color:#B8D8D8;"
                                          "border-radius:10px;"
                                          "border:1px solid #B8D8D8;"
                                          "display:inline-block;"
                                          "color:#000;"
                                          "padding:10px 10px;")
        self.phone_edittext.move(50, 150)
        self.phone_edittext.resize(200, 36)

        self.email_edittext = QLineEdit(self)
        self.email_edittext.setText("email")
        self.email_edittext.setAlignment(Qt.AlignCenter)
        self.email_edittext.setStyleSheet("background-color:#B8D8D8;"
                                          "border-radius:10px;"
                                          "border:1px solid #B8D8D8;"
                                          "display:inline-block;"
                                          "color:#000;"
                                          "padding:10px 10px;")
        self.email_edittext.move(50, 190)
        self.email_edittext.resize(200, 36)

        self.username_edittext = QLineEdit(self)
        self.username_edittext.setText("username")
        self.username_edittext.setAlignment(Qt.AlignCenter)
        self.username_edittext.setStyleSheet("background-color:#B8D8D8;"
                                             "border-radius:10px;"
                                             "border:1px solid #B8D8D8;"
                                             "display:inline-block;"
                                             "color:#000;"
                                             "padding:10px 10px;")
        self.username_edittext.move(50, 230)
        self.username_edittext.resize(200, 36)

        self.password_edittext = QLineEdit(self)
        self.password_edittext.setText("password")
        self.password_edittext.setAlignment(Qt.AlignCenter)
        self.password_edittext.setStyleSheet("background-color:#B8D8D8;"
                                             "border-radius:10px;"
                                             "border:1px solid #B8D8D8;"
                                             "display:inline-block;"
                                             "color:#000;"
                                             "padding:10px 10px;")
        self.password_edittext.move(50, 270)
        self.password_edittext.resize(200, 36)

        self.address_edittext = QLineEdit(self)
        self.address_edittext.setText("address")
        self.address_edittext.setAlignment(Qt.AlignCenter)
        self.address_edittext.setStyleSheet("background-color:#B8D8D8;"
                                            "border-radius:10px;"
                                            "border:1px solid #B8D8D8;"
                                            "display:inline-block;"
                                            "color:#000;"
                                            "padding:10px 10px;")
        self.address_edittext.move(50, 310)
        self.address_edittext.resize(200, 36)

        self.postal_code_edittext = QLineEdit(self)
        self.postal_code_edittext.setText("postal code")
        self.postal_code_edittext.setAlignment(Qt.AlignCenter)
        self.postal_code_edittext.setStyleSheet("background-color:#B8D8D8;"
                                                "border-radius:10px;"
                                                "border:1px solid #B8D8D8;"
                                                "display:inline-block;"
                                                "color:#000;"
                                                "padding:10px 10px;")
        self.postal_code_edittext.move(50, 350)
        self.postal_code_edittext.resize(200, 36)

        self.login_btn = QPushButton(self)
        self.login_btn.setText("add admin")
        self.login_btn.setGeometry(50, 430, 200, 50)
        self.login_btn.setStyleSheet("background-color:#FE5F55;"
                                     "border-radius:10px;"
                                     "border:1px solid #FE5F55;"
                                     "display:inline-block;"
                                     "color:#EEF5DB;"
                                     "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.login_btn.setFont(font)
        self.login_btn.clicked.connect(lambda: fields_validation(self.name_edittext.text(),
                                                                 self.phone_edittext.text(),
                                                                 self.username_edittext.text(),
                                                                 self.password_edittext.text(),
                                                                 self.email_edittext.text(),
                                                                 self.address_edittext.text(),
                                                                 self.postal_code_edittext.text(),
                                                                 Roles.ADMIN.value))


class UsersListWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        users_list = get_users_list()
        self.setMinimumSize(QSize(800, 200))
        self.setWindowTitle("USERS LIST")
        self.setGeometry(100, 100, 800, 300)

        table = QTableWidget(self)
        table.setColumnCount(len(users_list[0]))
        table.setRowCount(len(users_list))
        table.setMinimumWidth(1300)
        table.setMinimumHeight(1000)

        table.setHorizontalHeaderLabels(["user_id", "role", "full_name", "username",
                                         "email", "phone_number", "address",
                                         "postal_code", "joining_date"])

        for i in range(len(users_list)):
            for j in range(len(users_list[i])):
                table.setItem(i, j, QTableWidgetItem(str(users_list[i][j])))

        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        table.show()

        win = self.frameGeometry()
        pos = QDesktopWidget().availableGeometry().center()
        win.moveCenter(pos)
        self.move(win.topLeft())


class DeleteUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("REMOVE USER")
        self.setGeometry(100, 100, 300, 600)
        self.UiComponents()
        self.setStyleSheet("background-color : #4F6367")

    def UiComponents(self):
        # title
        self.title = QLabel(self)
        self.title.setText("REMOVE USER")
        self.title.setGeometry(20, 5, 260, 60)
        self.title.setStyleSheet("color : #FE5F55")
        self.title.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.title.setFont(font)

        self.username_edittext = QLineEdit(self)
        self.username_edittext.setText("username")
        self.username_edittext.setAlignment(Qt.AlignCenter)
        self.username_edittext.setStyleSheet("background-color:#B8D8D8;"
                                             "border-radius:10px;"
                                             "border:1px solid #B8D8D8;"
                                             "display:inline-block;"
                                             "color:#000;"
                                             "padding:10px 10px;")
        self.username_edittext.move(50, 110)
        self.username_edittext.resize(200, 36)

        self.remove_btn = QPushButton(self)
        self.remove_btn.setText("remove user")
        self.remove_btn.setGeometry(50, 430, 200, 50)
        self.remove_btn.setStyleSheet("background-color:#FE5F55;"
                                      "border-radius:10px;"
                                      "border:1px solid #FE5F55;"
                                      "display:inline-block;"
                                      "color:#EEF5DB;"
                                      "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.remove_btn.setFont(font)
        self.remove_btn.clicked.connect(lambda: remove_user(self.username_edittext.text()))


class ChangeCategoriesWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ABOUT CATEGORIES")
        self.setGeometry(100, 100, 300, 600)
        self.UiComponents()
        self.setStyleSheet("background-color : #4F6367")

    def UiComponents(self):
        # title
        self.title = QLabel(self)
        self.title.setText("ABOUT CATEGORIES")
        self.title.setGeometry(20, 5, 260, 60)
        self.title.setStyleSheet("color : #FE5F55")
        self.title.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(12)
        self.title.setFont(font)

        self.name_edittext = QLineEdit(self)
        self.name_edittext.setText("category name")
        self.name_edittext.setAlignment(Qt.AlignCenter)
        self.name_edittext.setStyleSheet("background-color:#B8D8D8;"
                                         "border-radius:10px;"
                                         "border:1px solid #B8D8D8;"
                                         "display:inline-block;"
                                         "color:#000;"
                                         "padding:10px 10px;")
        self.name_edittext.move(50, 110)
        self.name_edittext.resize(200, 36)

        self.add_btn = QPushButton(self)
        self.add_btn.setText("add category")
        self.add_btn.setGeometry(90, 155, 120, 40)
        self.add_btn.setStyleSheet("background-color:#FE5F55;"
                                   "border-radius:10px;"
                                   "border:1px solid #FE5F55;"
                                   "display:inline-block;"
                                   "color:#EEF5DB;"
                                   "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.add_btn.setFont(font)
        self.add_btn.clicked.connect(lambda: add_category(self.name_edittext.text()))

        self.re_name_edittext = QLineEdit(self)
        self.re_name_edittext.setText("category name")
        self.re_name_edittext.setAlignment(Qt.AlignCenter)
        self.re_name_edittext.setStyleSheet("background-color:#B8D8D8;"
                                            "border-radius:10px;"
                                            "border:1px solid #B8D8D8;"
                                            "display:inline-block;"
                                            "color:#000;"
                                            "padding:10px 10px;")
        self.re_name_edittext.move(50, 230)
        self.re_name_edittext.resize(200, 36)

        self.remove_btn = QPushButton(self)
        self.remove_btn.setText("remove category")
        self.remove_btn.setGeometry(90, 275, 120, 40)
        self.remove_btn.setStyleSheet("background-color:#FE5F55;"
                                      "border-radius:10px;"
                                      "border:1px solid #FE5F55;"
                                      "display:inline-block;"
                                      "color:#EEF5DB;"
                                      "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.remove_btn.setFont(font)
        self.remove_btn.clicked.connect(lambda: remove_category(self.re_name_edittext.text()))

        self.ed_before_edittext = QLineEdit(self)
        self.ed_before_edittext.setText("previous name")
        self.ed_before_edittext.setAlignment(Qt.AlignCenter)
        self.ed_before_edittext.setStyleSheet("background-color:#B8D8D8;"
                                              "border-radius:10px;"
                                              "border:1px solid #B8D8D8;"
                                              "display:inline-block;"
                                              "color:#000;"
                                              "padding:10px 10px;")
        self.ed_before_edittext.move(30, 350)
        self.ed_before_edittext.resize(100, 36)

        self.ed_after_edittext = QLineEdit(self)
        self.ed_after_edittext.setText("new name")
        self.ed_after_edittext.setAlignment(Qt.AlignCenter)
        self.ed_after_edittext.setStyleSheet("background-color:#B8D8D8;"
                                             "border-radius:10px;"
                                             "border:1px solid #B8D8D8;"
                                             "display:inline-block;"
                                             "color:#000;"
                                             "padding:10px 10px;")
        self.ed_after_edittext.move(160, 350)
        self.ed_after_edittext.resize(100, 36)

        self.edit_btn = QPushButton(self)
        self.edit_btn.setText("edit category")
        self.edit_btn.setGeometry(90, 395, 120, 40)
        self.edit_btn.setStyleSheet("background-color:#FE5F55;"
                                    "border-radius:10px;"
                                    "border:1px solid #FE5F55;"
                                    "display:inline-block;"
                                    "color:#EEF5DB;"
                                    "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.edit_btn.setFont(font)
        self.edit_btn.clicked.connect(lambda: edit_category_name(self.ed_before_edittext.text(),
                                                                 self.ed_after_edittext.text()))


class AddProductWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ADD PRODUCT")
        self.setGeometry(100, 100, 300, 600)
        self.UiComponents()
        self.setStyleSheet("background-color : #4F6367")

    def UiComponents(self):
        # title
        self.title = QLabel(self)
        self.title.setText("ADD PRODUCT")
        self.title.setGeometry(20, 5, 260, 60)
        self.title.setStyleSheet("color : #FE5F55")
        self.title.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.title.setFont(font)

        self.name_edittext = QLineEdit(self)
        self.name_edittext.setText("product name")
        self.name_edittext.setAlignment(Qt.AlignCenter)
        self.name_edittext.setStyleSheet("background-color:#B8D8D8;"
                                         "border-radius:10px;"
                                         "border:1px solid #B8D8D8;"
                                         "display:inline-block;"
                                         "color:#000;"
                                         "padding:10px 10px;")
        self.name_edittext.move(50, 110)
        self.name_edittext.resize(200, 36)

        self.category_edittext = QLineEdit(self)
        self.category_edittext.setText("category")
        self.category_edittext.setAlignment(Qt.AlignCenter)
        self.category_edittext.setStyleSheet("background-color:#B8D8D8;"
                                             "border-radius:10px;"
                                             "border:1px solid #B8D8D8;"
                                             "display:inline-block;"
                                             "color:#000;"
                                             "padding:10px 10px;")
        self.category_edittext.move(50, 150)
        self.category_edittext.resize(200, 36)

        self.count_edittext = QLineEdit(self)
        self.count_edittext.setText("count")
        self.count_edittext.setAlignment(Qt.AlignCenter)
        self.count_edittext.setStyleSheet("background-color:#B8D8D8;"
                                          "border-radius:10px;"
                                          "border:1px solid #B8D8D8;"
                                          "display:inline-block;"
                                          "color:#000;"
                                          "padding:10px 10px;")
        self.count_edittext.move(50, 190)
        self.count_edittext.resize(200, 36)

        self.price_edittext = QLineEdit(self)
        self.price_edittext.setText("price")
        self.price_edittext.setAlignment(Qt.AlignCenter)
        self.price_edittext.setStyleSheet("background-color:#B8D8D8;"
                                          "border-radius:10px;"
                                          "border:1px solid #B8D8D8;"
                                          "display:inline-block;"
                                          "color:#000;"
                                          "padding:10px 10px;")
        self.price_edittext.move(50, 230)
        self.price_edittext.resize(200, 36)

        self.add_btn = QPushButton(self)
        self.add_btn.setText("add product")
        self.add_btn.setGeometry(50, 430, 200, 50)
        self.add_btn.setStyleSheet("background-color:#FE5F55;"
                                   "border-radius:10px;"
                                   "border:1px solid #FE5F55;"
                                   "display:inline-block;"
                                   "color:#EEF5DB;"
                                   "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.add_btn.setFont(font)
        self.add_btn.clicked.connect(lambda: add_product(self.category_edittext.text(),
                                                         self.name_edittext.text(),
                                                         self.count_edittext.text(),
                                                         self.price_edittext.text()))


class DeleteProductWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("REMOVE PRODUCT")
        self.setGeometry(100, 100, 300, 600)
        self.UiComponents()
        self.setStyleSheet("background-color : #4F6367")

    def UiComponents(self):
        # title
        self.title = QLabel(self)
        self.title.setText("REMOVE PRODUCT")
        self.title.setGeometry(20, 5, 260, 60)
        self.title.setStyleSheet("color : #FE5F55")
        self.title.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.title.setFont(font)

        self.name_edittext = QLineEdit(self)
        self.name_edittext.setText("product name")
        self.name_edittext.setAlignment(Qt.AlignCenter)
        self.name_edittext.setStyleSheet("background-color:#B8D8D8;"
                                         "border-radius:10px;"
                                         "border:1px solid #B8D8D8;"
                                         "display:inline-block;"
                                         "color:#000;"
                                         "padding:10px 10px;")
        self.name_edittext.move(50, 110)
        self.name_edittext.resize(200, 36)

        self.remove_btn = QPushButton(self)
        self.remove_btn.setText("remove product")
        self.remove_btn.setGeometry(50, 430, 200, 50)
        self.remove_btn.setStyleSheet("background-color:#FE5F55;"
                                      "border-radius:10px;"
                                      "border:1px solid #FE5F55;"
                                      "display:inline-block;"
                                      "color:#EEF5DB;"
                                      "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.remove_btn.setFont(font)
        self.remove_btn.clicked.connect(lambda: delete_product(self.name_edittext.text()))


class EditProductWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EDIT PRODUCT")
        self.setGeometry(100, 100, 300, 600)
        self.UiComponents()
        self.setStyleSheet("background-color : #4F6367")

    def UiComponents(self):
        self.title = QLabel(self)
        self.title.setText("EDIT PRODUCT")
        self.title.setGeometry(20, 5, 260, 60)
        self.title.setStyleSheet("color : #FE5F55")
        self.title.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.title.setFont(font)

        self.name_edittext = QLineEdit(self)
        self.name_edittext.setText("previous name")
        self.name_edittext.setAlignment(Qt.AlignCenter)
        self.name_edittext.setStyleSheet("background-color:#B8D8D8;"
                                         "border-radius:10px;"
                                         "border:1px solid #B8D8D8;"
                                         "display:inline-block;"
                                         "color:#000;"
                                         "padding:10px 10px;")
        self.name_edittext.move(50, 100)
        self.name_edittext.resize(200, 36)

        self.new_name_edittext = QLineEdit(self)
        self.new_name_edittext.setText("new name")
        self.new_name_edittext.setAlignment(Qt.AlignCenter)
        self.new_name_edittext.setStyleSheet("background-color:#B8D8D8;"
                                             "border-radius:10px;"
                                             "border:1px solid #B8D8D8;"
                                             "display:inline-block;"
                                             "color:#000;"
                                             "padding:10px 10px;")
        self.new_name_edittext.move(50, 150)
        self.new_name_edittext.resize(200, 36)

        self.edit_name_btn = QPushButton(self)
        self.edit_name_btn.setText("edit name")
        self.edit_name_btn.setGeometry(65, 190, 175, 40)
        self.edit_name_btn.setStyleSheet("background-color:#FE5F55;"
                                         "border-radius:10px;"
                                         "border:1px solid #FE5F55;"
                                         "display:inline-block;"
                                         "color:#EEF5DB;"
                                         "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.edit_name_btn.setFont(font)
        self.edit_name_btn.clicked.connect(lambda: edit_name(self.new_name_edittext.text(),
                                                             self.name_edittext.text()))

        self.category_edittext = QLineEdit(self)
        self.category_edittext.setText("new category")
        self.category_edittext.setAlignment(Qt.AlignCenter)
        self.category_edittext.setStyleSheet("background-color:#B8D8D8;"
                                             "border-radius:10px;"
                                             "border:1px solid #B8D8D8;"
                                             "display:inline-block;"
                                             "color:#000;"
                                             "padding:10px 10px;")
        self.category_edittext.move(50, 240)
        self.category_edittext.resize(200, 36)

        self.edit_category_btn = QPushButton(self)
        self.edit_category_btn.setText("edit category")
        self.edit_category_btn.setGeometry(65, 280, 175, 40)
        self.edit_category_btn.setStyleSheet("background-color:#FE5F55;"
                                             "border-radius:10px;"
                                             "border:1px solid #FE5F55;"
                                             "display:inline-block;"
                                             "color:#EEF5DB;"
                                             "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.edit_category_btn.setFont(font)
        self.edit_category_btn.clicked.connect(lambda: edit_category(self.category_edittext.text(),
                                                                     self.name_edittext.text()))

        self.count_edittext = QLineEdit(self)
        self.count_edittext.setText("new count")
        self.count_edittext.setAlignment(Qt.AlignCenter)
        self.count_edittext.setStyleSheet("background-color:#B8D8D8;"
                                          "border-radius:10px;"
                                          "border:1px solid #B8D8D8;"
                                          "display:inline-block;"
                                          "color:#000;"
                                          "padding:10px 10px;")
        self.count_edittext.move(50, 330)
        self.count_edittext.resize(200, 36)

        self.edit_count_btn = QPushButton(self)
        self.edit_count_btn.setText("edit count")
        self.edit_count_btn.setGeometry(65, 370, 175, 40)
        self.edit_count_btn.setStyleSheet("background-color:#FE5F55;"
                                          "border-radius:10px;"
                                          "border:1px solid #FE5F55;"
                                          "display:inline-block;"
                                          "color:#EEF5DB;"
                                          "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.edit_count_btn.setFont(font)
        self.edit_count_btn.clicked.connect(lambda: edit_count(self.count_edittext.text(), self.name_edittext.text()))

        self.price_edittext = QLineEdit(self)
        self.price_edittext.setText("new price")
        self.price_edittext.setAlignment(Qt.AlignCenter)
        self.price_edittext.setStyleSheet("background-color:#B8D8D8;"
                                          "border-radius:10px;"
                                          "border:1px solid #B8D8D8;"
                                          "display:inline-block;"
                                          "color:#000;"
                                          "padding:10px 10px;")
        self.price_edittext.move(50, 420)
        self.price_edittext.resize(200, 36)

        self.edit_price_btn = QPushButton(self)
        self.edit_price_btn.setText("edit price")
        self.edit_price_btn.setGeometry(65, 460, 175, 40)
        self.edit_price_btn.setStyleSheet("background-color:#FE5F55;"
                                          "border-radius:10px;"
                                          "border:1px solid #FE5F55;"
                                          "display:inline-block;"
                                          "color:#EEF5DB;"
                                          "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.edit_price_btn.setFont(font)
        self.edit_price_btn.clicked.connect(lambda: edit_price(self.price_edittext.text(),
                                                               self.name_edittext.text()))


class AllOrdersWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color : #4F6367")
        self.controls = QWidget()
        self.controlsLayout = QVBoxLayout()
        self.setGeometry(300, 100, 800, 600)
        self.setWindowTitle('ALL USERS LIST')

        widget_names = []

        from codes.all_orders_widget import get_all_orders
        from codes.all_orders_widget import object_list

        ord_list = get_all_orders()
        obj_ord_list = object_list(ord_list)

        for ord in obj_ord_list:
            widget_names.append(ord.username)

        self.widgets = []

        titles = AllOrdersWidget("order_id", "username", "order_status",
                                 "total_price", "ordering_date", "updating_date")
        self.controlsLayout.addWidget(titles)

        for it in obj_ord_list:

            if str(it.order_status) == "-1":
                order_status = "canceled"
            elif str(it.order_status) == "1":
                order_status = "received"
            else:
                order_status = "preparing"

            item = AllOrdersWidget(str(it.order_id), it.username, order_status,
                                   str(it.total_price), it.ordering_date, it.updating_date)
            self.controlsLayout.addWidget(item)
            self.widgets.append(item)

        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.controlsLayout.addItem(spacer)
        self.controls.setLayout(self.controlsLayout)

        self.scroll = QScrollArea()
        self.scroll.setStyleSheet("background-color: #a7b1b3;")
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.controls)

        self.searchbar = QLineEdit()
        self.searchbar.setStyleSheet("color: black;"
                                     "background-color: #a7b1b3;"
                                     "padding: 6px")

        self.searchbar.textChanged.connect(self.update_display)

        self.completer = QCompleter(widget_names)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.searchbar.setCompleter(self.completer)

        container = QWidget()
        containerLayout = QVBoxLayout()
        containerLayout.addWidget(self.searchbar)
        containerLayout.addWidget(self.scroll)

        container.setLayout(containerLayout)
        self.setCentralWidget(container)

    def update_display(self, text):
        for widget in self.widgets:
            if text.lower() in widget.username.lower():
                widget.show()
            else:
                widget.hide()


class UserAccessesWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("user accesses")
        self.setGeometry(100, 100, 300, 400)
        self.UiComponents()
        self.setStyleSheet("background-color : #4F6367")
        self.wishlist_window = WishlistWindow()
        self.productsList_window = ProductsListWindow()
        self.ordersList_window = MyOrdersList()

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()

    def UiComponents(self):
        # title
        self.title = QLabel(self)
        self.title.setText("USER ACCESSES")
        self.title.setGeometry(20, 5, 260, 60)
        self.title.setStyleSheet("color : #FE5F55")
        self.title.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.title.setFont(font)

        self.wishlist_btn = QPushButton(self)
        self.wishlist_btn.setText("my wishlist")
        self.wishlist_btn.setGeometry(90, 70, 120, 40)
        self.wishlist_btn.setStyleSheet("background-color:#FE5F55;"
                                        "border-radius:10px;"
                                        "border:1px solid #FE5F55;"
                                        "display:inline-block;"
                                        "color:#EEF5DB;"
                                        "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.wishlist_btn.setFont(font)
        self.wishlist_btn.clicked.connect(lambda checked: self.toggle_window(self.wishlist_window))

        self.orders_btn = QPushButton(self)
        self.orders_btn.setText("my orders")
        self.orders_btn.setGeometry(90, 120, 120, 40)
        self.orders_btn.setStyleSheet("background-color:#FE5F55;"
                                      "border-radius:10px;"
                                      "border:1px solid #FE5F55;"
                                      "display:inline-block;"
                                      "color:#EEF5DB;"
                                      "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.orders_btn.setFont(font)
        self.orders_btn.clicked.connect(lambda checked: self.toggle_window(self.ordersList_window))

        self.products_list = QPushButton(self)
        self.products_list.setText("products list")
        self.products_list.setGeometry(90, 170, 120, 40)
        self.products_list.setStyleSheet("background-color:#FE5F55;"
                                         "border-radius:10px;"
                                         "border:1px solid #FE5F55;"
                                         "display:inline-block;"
                                         "color:#EEF5DB;"
                                         "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.products_list.setFont(font)
        self.products_list.clicked.connect(lambda checked: self.toggle_window(self.productsList_window))


class WishlistWindow(QWidget):
    def __init__(self):
        super(WishlistWindow, self).__init__()
        self.setWindowTitle("My Wishlist")
        self.setGeometry(100, 100, 300, 600)
        layout = show_wishlist()
        self.setLayout(layout)
        self.setStyleSheet("background-color : #4F6367")


class MyOrdersList(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color : #4F6367")
        self.controls = QWidget()
        self.controlsLayout = QVBoxLayout()

        from codes.my_orders_widget import get_my_orders
        from codes.my_orders_widget import object_list

        widget_names = []

        cur_user = load_current_user_data()

        if not cur_user:
            obj_list = []
        else:
            prev_list = get_my_orders(cur_user.user_id)
            obj_list = object_list(prev_list)

        for ord in obj_list:
            widget_names.append(str(ord.order_id))




        self.widgets = []

        titles = MyOrdersWidget("order_id", "order_status", "total_price", "ordering_date")
        self.controlsLayout.addWidget(titles)

        for it in obj_list:

            if str(it.order_status) == "-1":
                order_status = "canceled"
            elif str(it.order_status) == "1":
                order_status = "received"
            else:
                order_status = "preparing"

            item = MyOrdersWidget(str(it.order_id), order_status, str(it.total_price), str(it.ordering_date))
            self.controlsLayout.addWidget(item)
            self.widgets.append(item)

        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.controlsLayout.addItem(spacer)
        self.controls.setLayout(self.controlsLayout)

        self.scroll = QScrollArea()
        self.scroll.setStyleSheet("background-color: #a7b1b3;")
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.controls)

        self.searchbar = QLineEdit()
        self.searchbar.setStyleSheet("color: black;"
                                     "background-color: #a7b1b3;"
                                     "padding: 6px")

        self.searchbar.textChanged.connect(self.update_display)

        self.completer = QCompleter(widget_names)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.searchbar.setCompleter(self.completer)

        container = QWidget()
        containerLayout = QVBoxLayout()
        containerLayout.addWidget(self.searchbar)
        containerLayout.addWidget(self.scroll)

        container.setLayout(containerLayout)
        self.setCentralWidget(container)

        self.setGeometry(300, 100, 800, 600)
        self.setWindowTitle('Control Panel')

    def update_display(self, text):

        for widget in self.widgets:
            order_id = str(widget.order_id)
            if text.lower() in order_id.lower():
                widget.show()
            else:
                widget.hide()


class ReportsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("reports")
        self.setGeometry(100, 100, 300, 600)
        self.UiComponents()
        self.setStyleSheet("background-color : #4F6367")

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()

    def UiComponents(self):
        # title
        self.title = QLabel(self)
        self.title.setText("REPORTS")
        self.title.setGeometry(20, 5, 260, 60)
        self.title.setStyleSheet("color : #FE5F55")
        self.title.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.title.setFont(font)

        self.inventory_btn = QPushButton(self)
        self.inventory_btn.setText("Inventory Report")
        self.inventory_btn.setGeometry(90, 70, 120, 40)
        self.inventory_btn.setStyleSheet("background-color:#FE5F55;"
                                         "border-radius:10px;"
                                         "border:1px solid #FE5F55;"
                                         "display:inline-block;"
                                         "color:#EEF5DB;"
                                         "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.inventory_btn.setFont(font)
        self.inventory_btn.clicked.connect(lambda: get_inventory_report())

        self.total_sales_btn = QPushButton(self)
        self.total_sales_btn.setText("Total Sales")
        self.total_sales_btn.setGeometry(90, 120, 120, 40)
        self.total_sales_btn.setStyleSheet("background-color:#FE5F55;"
                                           "border-radius:10px;"
                                           "border:1px solid #FE5F55;"
                                           "display:inline-block;"
                                           "color:#EEF5DB;"
                                           "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.total_sales_btn.setFont(font)
        self.total_sales_btn.clicked.connect(lambda: get_total_sales())

        self.edit_reports_btn = QPushButton(self)
        self.edit_reports_btn.setText("Edit Reports")
        self.edit_reports_btn.setGeometry(90, 170, 120, 40)
        self.edit_reports_btn.setStyleSheet("background-color:#FE5F55;"
                                            "border-radius:10px;"
                                            "border:1px solid #FE5F55;"
                                            "display:inline-block;"
                                            "color:#EEF5DB;"
                                            "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.edit_reports_btn.setFont(font)
        self.edit_reports_btn.clicked.connect(lambda: get_edit_reports())


class ProductsListWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color : #4F6367")
        self.controls = QWidget()
        self.controlsLayout = QVBoxLayout()

        widget_names = []

        from codes.products_widget import get_products
        from codes.products_widget import object_list
        from codes.products_widget import save_wishlist_to_file
        pro_list = get_products()
        obj_pro_list = object_list(pro_list)
        # pro_list.sort(key=lambda y: y.name)

        for pro in obj_pro_list:
            widget_names.append(pro.name)

        self.widgets = []

        titles = ProWidget("name", "category", "price", "count")
        self.controlsLayout.addWidget(titles)

        for it in obj_pro_list:
            item = ProWidget(it.name, str(it.category), str(it.price), str(it.count))
            self.controlsLayout.addWidget(item)
            self.widgets.append(item)

        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.controlsLayout.addItem(spacer)
        self.controls.setLayout(self.controlsLayout)

        self.scroll = QScrollArea()
        self.scroll.setStyleSheet("background-color: #a7b1b3;")
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.controls)

        # Search bar.
        self.searchbar = QLineEdit()
        self.searchbar.setStyleSheet("color: black;"
                                     "background-color: #a7b1b3;"
                                     "padding: 6px")

        self.searchbar.textChanged.connect(self.update_display)

        # Adding Completer.
        self.completer = QCompleter(widget_names)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.searchbar.setCompleter(self.completer)

        self.submit_btn = QPushButton("submit")
        self.submit_btn.setStyleSheet("background-color:#FE5F55;"
                                      "border:1px solid #FE5F55;"
                                      "display:inline-block;"
                                      "color:#EEF5DB;"
                                      "padding:10px 10px;"
                                      "font-weight: bold;")
        self.submit_btn.clicked.connect(lambda: save_wishlist_to_file())

        # Add the items to VBoxLayout (applied to container widget)
        # which encompasses the whole window.
        container = QWidget()
        containerLayout = QVBoxLayout()
        containerLayout.addWidget(self.searchbar)
        containerLayout.addWidget(self.scroll)
        containerLayout.addWidget(self.submit_btn)

        container.setLayout(containerLayout)
        self.setCentralWidget(container)

        self.setGeometry(300, 100, 800, 600)
        self.setWindowTitle('PRODUCTS LIST')

    def update_display(self, text):

        for widget in self.widgets:
            if (text.lower() in widget.name.lower()) or \
                    (text.lower() in widget.count.lower()) or \
                    (text.lower() in widget.price.lower()) or \
                    (text.lower() in widget.category.lower()):
                widget.show()
            else:
                widget.hide()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("main window")
        self.setGeometry(100, 100, 300, 600)
        self.UiComponents()
        self.setStyleSheet("background-color : #4F6367")
        self.window1 = SignupWindow()
        self.window2 = LoginWindow()

    def UiComponents(self):
        # title
        self.title = QLabel(self)
        self.title.setText("MAIN WINDOW")
        self.title.setGeometry(20, 5, 260, 60)
        self.title.setStyleSheet("color : #FE5F55")
        self.title.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.title.setFont(font)

        self.add_admin_btn = QPushButton(self)
        self.add_admin_btn.setText("push for signup window")
        self.add_admin_btn.setGeometry(50, 70, 200, 40)
        self.add_admin_btn.setStyleSheet("background-color:#FE5F55;"
                                         "border-radius:10px;"
                                         "border:1px solid #FE5F55;"
                                         "display:inline-block;"
                                         "color:#EEF5DB;"
                                         "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.add_admin_btn.setFont(font)
        self.add_admin_btn.clicked.connect(
            lambda checked: self.toggle_window(self.window1)
        )
        # self.add_admin_btn.clicked.connect(lambda :)

        self.users_list_btn = QPushButton(self)
        self.users_list_btn.setText("push for login window")
        self.users_list_btn.setGeometry(50, 120, 200, 40)
        self.users_list_btn.setStyleSheet("background-color:#FE5F55;"
                                          "border-radius:10px;"
                                          "border:1px solid #FE5F55;"
                                          "display:inline-block;"
                                          "color:#EEF5DB;"
                                          "padding:2px 3px;")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.users_list_btn.setFont(font)
        self.users_list_btn.clicked.connect(
            lambda checked: self.toggle_window(self.window2)
        )

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
