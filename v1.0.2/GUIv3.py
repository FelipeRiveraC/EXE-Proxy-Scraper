import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import requests
from proxies import theweb
from bs4 import BeautifulSoup
import os
from random import choice
from selenium_scraper import SpyProxies, get_proxy3



class MiThread(Thread):
    def __init__(self, senal, texto, timeout):
        super().__init__()
        self.senal = senal
        self.texto = texto
        self.timeout = timeout
        self.threads = []
        self.url  = ["http://google.com", "https://www.facebook.com/", "https://twitter.com/", "https://github.com/", "https://www.similarweb.com/top-websites/"]
        self.url2 = theweb

    def run(self):
        a = self.check(self.texto)
        k = 90 #int(os.cpu_count())
        chunks = [a[int(x):int(x+int(len(a))/k)] for x in range(0, len(a), int(len(a)/k))]
        for i in range(k):
            self.threads.append(Thread(target=self.forth, args=[chunks[i]]))
        for thread in self.threads:
            thread.start()
        for thread in self.threads:
            thread.join()
        self.senal.emit("END")

    def forth(self, que):
        for proxy in que:
            proxx = {"http":proxy, "https":proxy}
            try:
                k = requests.get(choice(self.url), proxies = proxx, timeout=self.timeout)
                print("good")
                self.senal.emit(proxy+"\n")
            except:
                try:
                    k = requests.get(choice(self.url2), proxies = proxx, timeout=self.timeout)
                    print("good 2")
                    self.senal.emit(proxy+"\n")
                except:
                    [print("bad")]
     
    def check(self, proxiesk):
        lis7 = proxiesk.split()
        return lis7



class ScrapeTH(Thread):
    def __init__(self, senal):
        super().__init__()
        self.senal = senal
    def run(self):
        list2 = self.get_prox()
        kkk = SpyProxies()
        list2 += kkk.split()
        for proxy in list2:
            if len(proxy) >= len("36.91.28.210:8080"):
                self.senal.emit(proxy+"\n")

        get3 = get_proxy3()
        for proxy in get3.split():
            self.senal.emit(proxy+"\n")
                
    def get_prox(self):

        url = "https://www.sslproxies.org/"
        get_url = requests.get(url)
        soup = BeautifulSoup(get_url.content, "html.parser")
        lista = [i.text for i in soup.find_all('td')[::8]]
        lista_port = [i.text for i in soup.find_all('td')[1::8]]
        zipp = zip(lista, lista_port)
        list2 = list(map(lambda x: x[0]+":"+x[1], list(zipp)))
        return list2

class MiVentana(QtCore.QObject):
    signal = QtCore.pyqtSignal(str)
    signal2 = QtCore.pyqtSignal(str)
    cantidad = 0
    cantidad2= 0
    texter = ""
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(632, 524)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 20, 351, 71))
        self.progressbar = QtWidgets.QLabel(Form)
        self.progressbar.setGeometry(QtCore.QRect(60, 90, 360, 30))
        self.progressbar2 = QtWidgets.QLabel(Form)
        self.progressbar2.setGeometry(QtCore.QRect(380, 90, 360, 30))
        font = QtGui.QFont()
        font2 = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font2.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.progressbar2.setFont(font2)
        self.progressbar.setFont(font2)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(430, 70, 121, 16))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 170, 256, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(350, 170, 256, 291))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.setText(self.textBrowser_2.toPlainText())
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(350, 110, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 470, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 470, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 470, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 470, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(530, 140, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(510, 470, 21, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(430, 470, 121, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(120, 470, 81, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Proxy Scraper"))
        self.progressbar.setText(_translate("Form", "Scraped: "))
        self.progressbar2.setText(_translate("Form", "Checked:"))
        self.label_2.setText(_translate("Form", "by rivem0dz"))
        self.label_3.setText(_translate("Form", "Scrape"))
        self.label_4.setText(_translate("Form", "Check"))
        self.pushButton.setText(_translate("Form", "Scrape!"))
        self.pushButton_2.setText(_translate("Form", "Clear"))
        self.pushButton_3.setText(_translate("Form", "Save to file"))
        self.pushButton_4.setText(_translate("Form", "Clear"))
        self.pushButton_5.setText(_translate("Form", "Upload file"))
        self.pushButton_6.setText(_translate("Form", "Start check"))
        self.lineEdit.setText(_translate("Form", "5"))
        self.label_5.setText(_translate("Form", "Custom timeout:"))
        self.pushButton_7.setText(_translate("Form", "Paste in check"))
        self.signal.connect(self.checkear)
        self.signal2.connect(self.scrapear)
        self.pushButton_6.clicked.connect(self.ejecutarcheck)
        self.pushButton.clicked.connect(self.ejecutar_scrape)
        self.pushButton_7.clicked.connect(self.pegar)
        self.pushButton_3.clicked.connect(self.save1)
        self.pushButton_2.clicked.connect(self.clear1)
        self.pushButton_4.clicked.connect(self.clear2)
    
    def clear1(self):
        self.cantidad = 0
        self.textBrowser.setText("")
    def clear2(self):
        self.cantidad2 = 0
        self.textBrowser_2.setText("")
    def save1(self):
        with open("proxies_Scrape.txt", "w") as s:
            s.write(self.textBrowser.toPlainText())
    def pegar(self):
        self.textBrowser_2.setText(self.textBrowser.toPlainText())
    def ejecutar_scrape(self):
        self.pushButton.setText("Scraping...")
        self.threadScrape = ScrapeTH(self.signal2)
        self.threadScrape.start()

    def scrapear(self, evento):
        self.cantidad += 1
        self.progressbar.setText(f"Scraped: {self.cantidad}")
        self.textBrowser.setText(self.textBrowser.toPlainText()  + evento)
        self.pushButton.setText("Scrape!")


    def checkear(self, evento):
        if evento != "END":
            self.cantidad2 += 1
            self.progressbar2.setText(f"Checked: {self.cantidad2}")
            self.textBrowser_2.setText(self.textBrowser_2.toPlainText() + evento)
        else:
            self.pushButton_6.setText("Start check")

    def ejecutarcheck(self):
        self.texter = self.textBrowser_2.toPlainText()
        self.textBrowser_2.setText("")
        self.pushButton_6.setText("Checking...")
        self.thread = MiThread(self.signal, self.texter, int(self.lineEdit.text()))
        self.thread.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = MiVentana()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
