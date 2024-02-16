import xlsxwriter
from codes.products import get_products
import mysql
import datetime


def get_orders():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    sql = "SELECT order_id, price FROM orders WHERE order_status = 1"

    mycursor.execute(sql)

    return_list = mycursor.fetchall()

    mydb.commit()

    return return_list


def get_reports():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1457914neg",
        database="sql_store"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM edit_reports"

    mycursor.execute(sql)

    return_list = mycursor.fetchall()

    mydb.commit()

    return return_list


def get_inventory_report():
    workbook = xlsxwriter.Workbook("inventory.xlsx")
    worksheet = workbook.add_worksheet()

    # set format
    head_format = workbook.add_format({'bold': True})
    head_format.set_center_across()
    head_format.set_bg_color('#FFFF00')
    head_format.set_border()

    cell_format = workbook.add_format()
    cell_format.set_center_across()
    cell_format.set_border()

    # set size
    worksheet.set_column(0, 1, 15)
    worksheet.set_column(0, 2, 11)

    # set title
    worksheet.write(0, 0, "product_id", head_format)
    worksheet.write(0, 1, "name", head_format)
    worksheet.write(0, 2, "category_id", head_format)
    worksheet.write(0, 3, "count", head_format)
    worksheet.write(0, 4, "price", head_format)

    product_list = get_products()

    row = 1
    col = 0
    for item in product_list:
        worksheet.write(row, col, item[0], cell_format)
        worksheet.write(row, col + 1, item[2], cell_format)
        worksheet.write(row, col + 2, item[1], cell_format)
        worksheet.write(row, col + 3, item[3], cell_format)
        worksheet.write(row, col + 4, item[4], cell_format)

        row += 1

    workbook.close()
    print("excel file 'inventory.xlsx' created successfully")


def get_total_sales():
    orders_list = get_orders()

    workbook = xlsxwriter.Workbook("total_sales.xlsx")
    worksheet = workbook.add_worksheet()

    head_format = workbook.add_format({'bold': True})
    head_format.set_center_across()
    head_format.set_bg_color('#FFFF00')
    head_format.set_border()

    cell_format = workbook.add_format()
    cell_format.set_center_across()
    cell_format.set_border()

    result_format = workbook.add_format({'bold': True})
    result_format.set_center_across()
    result_format.set_bg_color('#18de18')
    result_format.set_border()

    worksheet.write(0, 0, "order_id", head_format)
    worksheet.write(0, 1, "price", head_format)

    row = 1
    col = 0
    for order_id, total_price in orders_list:
        worksheet.write(row, col, order_id, cell_format)
        worksheet.write(row, col + 1, total_price, cell_format)
        row += 1

    sum_row = "=SUM(B2:B" + str(row) + ")"

    worksheet.write(row, 0, 'Total', result_format)
    worksheet.write(row, 1, sum_row, result_format)

    workbook.close()
    print("excel file 'total_sales.xlsx' created successfully")


def get_edit_reports():
    workbook = xlsxwriter.Workbook("edit_reports.xlsx")
    worksheet = workbook.add_worksheet()

    # set format
    head_format = workbook.add_format({'bold': True})
    head_format.set_center_across()
    head_format.set_bg_color('#FFFF00')
    head_format.set_border()

    cell_format = workbook.add_format()
    cell_format.set_center_across()
    cell_format.set_border()

    # set size
    worksheet.set_column(0, 1, 10)
    worksheet.set_column(2, 2, 20)
    worksheet.set_column(3, 3, 50)


    # set title
    worksheet.write(0, 0, "report_id", head_format)
    worksheet.write(0, 1, "product_id", head_format)
    worksheet.write(0, 2, "last update date", head_format)
    worksheet.write(0, 3, "description", head_format)

    reports_list = get_reports()

    ts = '2013-01-12 15:27:43'
    f = '%Y-%m-%d %H:%M:%S'

    datetime.datetime.strptime(ts, f)
    datetime.datetime(2013, 1, 12, 15, 27, 43)

    row = 1
    col = 0
    for item in reports_list:
        worksheet.write(row, col, item[0], cell_format)
        worksheet.write(row, col + 1, item[1], cell_format)
        worksheet.write(row, col + 2, item[2].strftime(f), cell_format)
        worksheet.write(row, col + 3, item[3], cell_format)

        row += 1

    workbook.close()
    print("excel file 'edit_reports.xlsx' created successfully")
