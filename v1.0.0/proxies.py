import requests
from bs4 import BeautifulSoup
from random import choice

def get_proxy():
    url = "https://www.sslproxies.org/"
    get_url = requests.get(url)
    soup = BeautifulSoup(get_url.content, "html.parser")
    lista = [i.text for i in soup.find_all('td')[::8]]
    lista_port = [i.text for i in soup.find_all('td')[1::8]]
    zipp = zip(lista, lista_port)
    list2 = list(map(lambda x: x[0]+":"+x[1], list(zipp)))
    a = ""
    for proxy in list2:
        if len(proxy) >= len("36.91.28.210:8080"):
            a += f"{proxy}\n"
    return a

def get_proxy2():
    url = "http://www.sslproxies24.top/"
    get_url = requests.get(url)
    soup = BeautifulSoup(get_url.content, "html.parser")
    lista = soup.find_all("a", href=True)
    lista2 = [element["href"] for element in soup.find_all("a", href=True) if element["href"].startswith("http://www.sslproxies24.top/20") and "#" not in element["href"] and element["href"]]   
    return lista2
def get_proxy2f(url2):
    url = url2
    get_url = requests.get(url)
    soup = BeautifulSoup(get_url.content, "html.parser")
    lista = soup.find("pre", class_="alt2")
    return lista.text

def full_proxies():
    a = ""
    for element in get_proxy2():
        try:
            a += get_proxy2f(element)
        except:
            pass

    a += "\n"
    a += get_proxy()

    return a

def savef(proxies):
    with open("scrape.txt", "w") as s:
        s.write(proxies)