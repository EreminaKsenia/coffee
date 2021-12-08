import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.show_table()
        self.modified = {}
        self.titles = None

    def show_table(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute("SELECT * FROM coffee").fetchall()
        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))

        title1 = QTableWidgetItem()
        title1.setText("ID")
        self.tableWidget.setHorizontalHeaderItem(0, title1)
        title2 = QTableWidgetItem()
        title2.setText("Название сорта")
        self.tableWidget.setHorizontalHeaderItem(1, title2)
        title3 = QTableWidgetItem()
        title3.setText("Степень обжарки")
        self.tableWidget.setHorizontalHeaderItem(2, title3)
        title4 = QTableWidgetItem()
        title4.setText("Молотый/в зернах")
        self.tableWidget.setHorizontalHeaderItem(3, title4)
        title5 = QTableWidgetItem()
        title5.setText("Описание вкуса")
        self.tableWidget.setHorizontalHeaderItem(4, title5)
        title6 = QTableWidgetItem()
        title6.setText("Цена")
        self.tableWidget.setHorizontalHeaderItem(5, title6)
        title7 = QTableWidgetItem()
        title7.setText("Объем упаковки(г)")
        self.tableWidget.setHorizontalHeaderItem(6, title7)

        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())