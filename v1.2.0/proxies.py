import os
import queue
import socket
import urllib
from random import choice
from threading import Thread
import requests
from bs4 import BeautifulSoup

def get_proxy(listn, senal):
    url = "https://free-proxy-list.net/"
    a = requests.get(url)
    soup = BeautifulSoup(a.text, "html.parser")
    find = soup.find("div", id="raw")
    k = find.text.split()
    for i in range(11):
        del k[0]
    for i in k:
        if i[0].isnumeric() and i.count(".") == 3:
            senal.emit(i + "\n")
    print(len(listn))

def get_proxy22(listn, senal):
    url = "http://www.httptunnel.ge/ProxyListForFree.aspx"
    a = requests.get(url)
    soup = BeautifulSoup(a.text, "html.parser")
    find = soup.find_all("a")#, id="ctl00_ContentPlaceHolder1_GridViewNEW_ctl02_HyperLink2")
    for i in find:
        if i.text.count(".") == 3:
            senal.emit(str(i.text) + "\n")


