import sys
from PyQt5.QtWidgets import *
import pickle


def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setStyleSheet("background-color: mistyrose")
    layout = QGridLayout()
    productLabel = QLabel()
    costLabel = QLabel()
    prodLine = QLineEdit()
    costLine = QLineEdit()
    productLabel.setText("Item Name:")
    costLabel.setText("Cost:")
    dict = {}

    def add():
        p = prodLine.text()
        c = costLine.text()
        dict[p] = float(c)
        row = table.rowCount()
        table.setRowCount(row + 1)
        pcell = QTableWidgetItem(p)
        ccell = QTableWidgetItem(c)
        table.setItem(row, 0, pcell)
        table.setItem(row, 1, ccell)
        print(dict)

    def delete():
        selected = table.selectedItems()
        name = selected[0].text()
        dict.pop(name)
        selectedIndex = table.selectedIndexes()
        rowNo = selectedIndex[0].row()
        table.removeRow(rowNo)
        print(dict)

    def save():
        file = open("data1.pickle", "wb")
        pickle.dump(dict, file)
        file.close()
        print("data saved")

    def upload():
        file = open("data1.pickle", "wb")
        temp = pickle.load(file)
        for name, cost in temp.items():
            print(name, cost)
            dict[name] = cost
            row = table.rowCount()
            table.setRowCount(row + 1)
            pcell = QTableWidgetItem(name)
            ccell = QTableWidgetItem(cost)
            table.setItem(row, 0, pcell)
            table.setItem(row, 1, ccell)
        file.close()

    def bill():
        file = open("data1.pickle", "rb")
        temp = pickle.load(file)
        sum = 0
        for name, cost in temp.items():
            print(name, cost)
            sum = sum + float(cost)
        msg = QMessageBox()
        msg.setWindowTitle("Bill Info:")
        msg.setText("your bill is" + str(sum))
        x = msg.exec_()
        file.close()
        
    addButton = QPushButton()
    addButton.setText("ADD RECORD")
    addButton.clicked.connect(add)
    delButton = QPushButton()
    delButton.setText("DELETE RECORD")
    delButton.clicked.connect(delete)
    saveButton = QPushButton()
    saveButton.setText("Save RECORD")
    saveButton.clicked.connect(save)
    uploadButton = QPushButton()
    uploadButton.setText("Upload RECORD")
    uploadButton.clicked.connect(upload)
    billButton = QPushButton()
    billButton.setText("Bill Amount")
    billButton.clicked.connect(bill)
    table = QTableWidget()
    table.setColumnCount(2)
    row = table.rowCount()
    table.setHorizontalHeaderLabels(["Product Name", "Cost"])
    layout.addWidget(productLabel, 1, 1)
    layout.addWidget(prodLine, 1, 2)
    layout.addWidget(costLabel, 2, 1)
    layout.addWidget(costLine, 2, 2)
    layout.addWidget(addButton, 3, 1)
    layout.addWidget(delButton, 3, 2)
    layout.addWidget(saveButton, 3, 3)
    layout.addWidget(uploadButton, 3, 4)
    layout.addWidget(billButton, 1, 3)
    layout.addWidget(table, 4, 2)
    w.setLayout(layout)
    w.resize(830, 350)
    w.setWindowTitle("E-commerce Application")
    w.move(50, 200)
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
