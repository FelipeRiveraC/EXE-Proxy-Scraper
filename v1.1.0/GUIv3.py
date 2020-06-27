import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import requests
from proxies import theweb, get_proxy, get_proxy22
from bs4 import BeautifulSoup
import os
from random import choice
from selenium_scraper import SpyProxies, get_proxy3

# https://cracked.to/Thread-Best-Free-Proxy-Sources

class MiThread(Thread):
    def __init__(self, senal, texto, timeout, threads):
        super().__init__()
        self.senal = senal
        self.texto = texto
        self.timeout = timeout
        self.threadsa = threads
        self.threads = []
        self.url  = ["http://google.com", "https://www.facebook.com/", "https://twitter.com/", "https://github.com/", "https://www.similarweb.com/top-websites/"]
        self.url2 = theweb

    def run(self):
        a = self.check(self.texto)
        k = self.threadsa
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
                    self.senal.emit("BAD")
                    print("bad")
     
    def check(self, proxiesk):
        lis7 = proxiesk.split()
        return lis7

class ScrapeTH(Thread):
    def __init__(self, senal):
        super().__init__()
        self.senal = senal
        self.threadsl = []
        self.result1 = []

    def run(self):
        self.threadsl.append(Thread(target=get_proxy, args=[self.result1]))
        self.threadsl.append(Thread(target=self.get_prox, args=[self.result1]))
        self.threadsl.append(Thread(target=SpyProxies, args=[self.result1]))
        self.threadsl.append(Thread(target=get_proxy3, args=[self.result1]))
        self.threadsl.append(Thread(target=get_proxy22, args=[self.result1]))

        for threa in self.threadsl:
            threa.start()
        for threa in self.threadsl:
            threa.join()


        for proxy in self.result1:
            try:
                if proxy.count(".") == 3 and proxy.count(":") and proxy[0].isnumeric() == 1:
                    self.senal.emit(proxy+"\n")
            except:
                pass
        self.senal.emit("END")
                
    def get_prox(self, listn):

        url = "https://www.sslproxies.org/"
        get_url = requests.get(url)
        soup = BeautifulSoup(get_url.content, "html.parser")
        lista = [i.text for i in soup.find_all('td')[::8]]
        lista_port = [i.text for i in soup.find_all('td')[1::8]]
        zipp = zip(lista, lista_port)
        list2 = list(map(lambda x: x[0]+":"+x[1], list(zipp)))
        print(len(list2))
        for i in list2:
            listn.append(i)
        return list2

class MiVentana(QtCore.QObject):
    signal = QtCore.pyqtSignal(str)
    signal2 = QtCore.pyqtSignal(str)
    cantidadscraped = 0
    cantidadchecked= 0
    cantidadbad = 0
    texter = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 190, 771, 281))
        self.textBrowser.setObjectName("textBrowser")
        self.scrape = QtWidgets.QPushButton(self.centralwidget)
        self.scrape.setGeometry(QtCore.QRect(10, 160, 75, 23))
        self.scrape.setObjectName("scrape")
        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(90, 160, 75, 23))
        self.check.setObjectName("check")
        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(610, 160, 81, 23))
        self.upload.setObjectName("upload")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 160, 81, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(140, 0, 541, 61))
        font = QtGui.QFont()
        font.setFamily("Sketch 3D")
        font.setPointSize(40)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 70, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 90, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 130, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(300, 70, 191, 81))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.status = QtWidgets.QLabel(self.frame)
        self.status.setGeometry(QtCore.QRect(100, 0, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setObjectName("status")
        self.ascraped = QtWidgets.QLabel(self.frame)
        self.ascraped.setGeometry(QtCore.QRect(100, 20, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ascraped.setFont(font)
        self.ascraped.setObjectName("ascraped")
        self.achecked = QtWidgets.QLabel(self.frame)
        self.achecked.setGeometry(QtCore.QRect(100, 40, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.achecked.setFont(font)
        self.achecked.setObjectName("achecked")
        self.abad = QtWidgets.QLabel(self.frame)
        self.abad.setGeometry(QtCore.QRect(100, 60, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.abad.setFont(font)
        self.abad.setObjectName("abad")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(70, 0, 20, 91))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 10, 201, 16))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(0, 30, 201, 16))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(0, 50, 201, 16))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.setthreads = QtWidgets.QLineEdit(self.centralwidget)
        self.setthreads.setGeometry(QtCore.QRect(110, 479, 113, 21))
        self.setthreads.setObjectName("setthreads")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 480, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(610, 481, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.settimeout = QtWidgets.QLineEdit(self.centralwidget)
        self.settimeout.setGeometry(QtCore.QRect(670, 480, 113, 21))
        self.settimeout.setObjectName("settimeout")
        self.autor = QtWidgets.QLabel(self.centralwidget)
        self.autor.setGeometry(QtCore.QRect(600, 50, 341, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.autor.setFont(font)
        self.autor.setObjectName("autor")
        self.resetstat = QtWidgets.QPushButton(self.centralwidget)
        self.resetstat.setGeometry(QtCore.QRect(360, 160, 75, 23))
        self.resetstat.setObjectName("resetstat")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(360, 480, 81, 23))
        self.save.setObjectName("save")
        self.frame.raise_()
        self.textBrowser.raise_()
        self.scrape.raise_()
        self.check.raise_()
        self.upload.raise_()
        self.pushButton_4.raise_()
        self.titulo.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.setthreads.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.settimeout.raise_()
        self.autor.raise_()
        self.resetstat.raise_()
        self.save.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_to_file = QtWidgets.QAction(MainWindow)
        self.actionSave_to_file.setObjectName("actionSave_to_file")
        self.menuOptions.addAction(self.actionSave_to_file)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scrape.setText(_translate("MainWindow", "Scrape!"))
        self.check.setText(_translate("MainWindow", "Check!"))
        self.upload.setText(_translate("MainWindow", "Upload file..."))
        self.pushButton_4.setText(_translate("MainWindow", "Clear"))
        self.titulo.setText(_translate("MainWindow", "EXE-Proxy Scraper"))
        self.label_2.setText(_translate("MainWindow", "Status"))
        self.label_3.setText(_translate("MainWindow", "Scraped"))
        self.label_4.setText(_translate("MainWindow", "Checked"))
        self.label_5.setText(_translate("MainWindow", "Bad"))
        self.status.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Not Working...</span></p></body></html>"))
        self.ascraped.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00aa00;\">0</span></p></body></html>"))
        self.achecked.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00aa00;\">0</span></p></body></html>"))
        self.abad.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">0</span></p></body></html>"))
        self.setthreads.setText(_translate("MainWindow", "50"))
        self.label_10.setText(_translate("MainWindow", "Set Threads:"))
        self.label_11.setText(_translate("MainWindow", "Timeout:"))
        self.settimeout.setText(_translate("MainWindow", "5"))
        self.autor.setText(_translate("MainWindow", "by rivem0dz"))
        self.resetstat.setText(_translate("MainWindow", "Reset stats"))
        self.save.setText(_translate("MainWindow", "Save to file"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionSave_to_file.setText(_translate("MainWindow", "Save to file"))
        self.scrape.clicked.connect(self.ejecutar_scrape)
        self.signal.connect(self.scrapear)
        self.signal2.connect(self.checkear)
        self.check.clicked.connect(self.ejecutarcheck)
        self.resetstat.clicked.connect(self.resetall)
        self.save.clicked.connect(self.SaveToFile)
        self.upload.clicked.connect(self.Upload)
        self.pushButton_4.clicked.connect(self.Clear)
    def Upload(self):
        with open("EXE-Proxies_HERE.txt", "r") as s:
            az = s.readlines()
            self.textBrowser.setText("".join(az))
    def SaveToFile(self):
        x = QtWidgets.QMessageBox()
        x.setText("File Saved!")
        a = self.textBrowser.toPlainText()
        with open("EXE-Proxies_HERE.txt", "w") as s:
            s.write(a)
        z = x.exec_()

    def Clear(self):
        self.textBrowser.setText("")
    
    def resetall(self):
        self.cantidadscraped = 0
        self.cantidadchecked = 0
        self.cantidadbad = 0
        self.ascraped.setText("<html><head/><body><p><span style=\" color:#00aa00;\">0</span></p></body></html>")
        self.achecked.setText("<html><head/><body><p><span style=\" color:#00aa00;\">0</span></p></body></html>")
        self.abad.setText("<html><head/><body><p><span style=\" color:#ff0000;\">0</span></p></body></html>")

    def ejecutar_scrape(self):
        self.cantidadscraped = 0
        self.textBrowser.setText("")
        self.ascraped.setText("<html><head/><body><p><span style=\" color:#00aa00;\">0</span></p></body></html>")
        self.status.setText("<html><head/><body><p><span style=\" color:#00aa00;\">Working...</span></p></body></html>")
        self.scrape.setText("Scraping...")
        self.threadScrape = ScrapeTH(self.signal)
        self.threadScrape.start()
    
    def scrapear(self, evento):
        if evento != "END":
            self.status.setText("<html><head/><body><p><span style=\" color:#00aa00;\">Working...</span></p></body></html>")
            self.cantidadscraped += 1
            self.ascraped.setText(f"<html><head/><body><p><span style=\" color:#00aa00;\">{self.cantidadscraped}</span></p></body></html>")
            self.textBrowser.setText(self.textBrowser.toPlainText()  + evento)
        else:
            print("END")
            self.status.setText("<html><head/><body><p><span style=\" color:#ff0000;\">Not Working...</span></p></body></html>")
            self.scrape.setText("Scrape!")

    def ejecutarcheck(self):
        self.cantidadbad = 0
        self.cantidadchecked =0
        self.status.setText("<html><head/><body><p><span style=\" color:#00aa00;\">Working...</span></p></body></html>")
        self.texter = self.textBrowser.toPlainText()
        self.textBrowser.setText("")
        self.check.setText("Checking...")
        self.thread = MiThread(self.signal2, self.texter, int(self.settimeout.text()), int(self.setthreads.text()))
        self.thread.start()

    def checkear(self, evento):
        if evento != "END" and evento != "BAD":
            self.cantidadchecked += 1
            self.achecked.setText(f"<html><head/><body><p><span style=\" color:#00aa00;\">{self.cantidadchecked}</span></p></body></html>")
            self.textBrowser.setText(self.textBrowser.toPlainText() + evento)
        elif evento == "BAD":
            self.cantidadbad += 1
            self.abad.setText(f"<html><head/><body><p><span style=\" color:#ff0000;\">{self.cantidadbad}</span></p></body></html>")
        else:
            self.check.setText("Check!")
            self.status.setText("<html><head/><body><p><span style=\" color:#ff0000;\">Not Working...</span></p></body></html>")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = MiVentana()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())