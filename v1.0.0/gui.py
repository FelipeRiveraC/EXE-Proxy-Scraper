from PyQt5 import QtCore, QtGui, QtWidgets
from proxies import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(310, 432)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 0, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(220, 50, 111, 20))
        self.label_2.setObjectName("label_2")
        self.proxies = QtWidgets.QTextBrowser(Form)
        self.proxies.setGeometry(QtCore.QRect(30, 190, 256, 192))
        self.proxies.setObjectName("proxies")
        self.Scrape = QtWidgets.QPushButton(Form)
        self.Scrape.setGeometry(QtCore.QRect(30, 160, 75, 23))
        self.Scrape.setObjectName("Scrape")
        self.clear1 = QtWidgets.QPushButton(Form)
        self.clear1.setGeometry(QtCore.QRect(30, 390, 75, 23))
        self.clear1.setObjectName("clear")
        self.savetofile = QtWidgets.QPushButton(Form)
        self.savetofile.setGeometry(QtCore.QRect(210, 390, 75, 23))
        self.savetofile.setObjectName("savetofile")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 80, 251, 61))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.info = QtWidgets.QLabel(self.frame)
        self.info.setGeometry(QtCore.QRect(10, -10, 231, 41))
        self.info.setObjectName("info")
        self.donate = QtWidgets.QLabel(self.frame)
        self.donate.setGeometry(QtCore.QRect(10, 30, 240, 16))
        self.donate.setObjectName("donate")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Proxy Scraper by rivem0dz", "Proxy Scraper by rivem0dz"))
        self.label.setText(_translate("Form", "Proxy - Scraper"))
        self.label_2.setText(_translate("Form", "by rivem0dz"))
        self.Scrape.setText(_translate("Form", "Scrape!"))
        self.clear1.setText(_translate("Form", "Clear"))
        self.savetofile.setText(_translate("Form", "Save to file"))
        self.info.setText(_translate("Form", "Proxy scraper by rivem0dz. Powered by Python."))
        self.donate.setText(_translate("Form", "BTC: 1KvuQdrVoSqnGiLLb4KVtHXCgUPPujrNDC"))
        self.Scrape.clicked.connect(self.proxiez)
        self.clear1.clicked.connect(self.clear2)
        self.savetofile.clicked.connect(self.savefz)

    def proxiez(self):
        self.proxies.setText(full_proxies())
    
    def clear2(self):
        self.proxies.setText("")
    
    def savefz(self):
        with open("scrape.txt", "w") as s:
            s.write(self.proxies.toPlainText())
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Done!")
        msg.setText("file scrape.txt saved!")
        x = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
