import sys
from PyQt5 import QtWidgets, QtGui
import designfile
import iptorrent

class myApp(QtWidgets.QMainWindow, designfile.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.datatable = []

        self.pushButton.clicked.connect(self.get_data)

        self.setWindowIcon(QtGui.QIcon('ipt-icon.png'))
        self.setWindowTitle("IpTorrent")

        self.tableWidget.setColumnWidth(0, 600)
        self.tableWidget.setColumnWidth(1, 129) # Columns
        self.tableWidget.setColumnWidth(2, 100)
    
    def get_data(self):
        self.clear_data()
        ipaddress = self.lineEditIP.text()
        if not is_valid(ipaddress):
            return
        for obj in iptorrent.main(ipaddress):
            if obj[1].strip() == "": self.datatable.append({"torrent": obj[0], "category": "Нет категории", "size": obj[2]})
            else: self.datatable.append({"torrent": obj[0], "category": obj[1], "size": obj[2]})
        row = 0
        self.tableWidget.setRowCount(len(self.datatable))
        for torr in self.datatable:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(torr.get("torrent")))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(torr.get("category")))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(torr.get("size")))
            row += 1
    
    def clear_data(self):
        self.datatable = []
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(self.tableWidget.rowCount()-1)


def is_valid(string: str):
    strsplit = string.split(".")
    if len(strsplit) != 4:
        return False
    if strsplit[0].isnumeric() and strsplit[1].isnumeric() and strsplit[2].isnumeric() and strsplit[3].isnumeric() and int(strsplit[0]) < 256 and int(strsplit[1]) < 256 and int(strsplit[2]) < 256 and  int(strsplit[3]) < 256:
        return True
    return False

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    
    app.exec_()

if __name__ == '__main__':
    main()