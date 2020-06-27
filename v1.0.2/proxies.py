import os
import queue
import socket
import urllib
from random import choice
from threading import Thread

import requests
from bs4 import BeautifulSoup


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
    a = get_proxy()

    return a

def check(proxiesk, que, timeoutk):
    a = ""
    url = "https://api.ipify.org"
    lis7 = proxiesk.split()
    for proxy in lis7:
        proxx = {"http":proxy, "https":proxy}
        #print(proxx)
        try:
            requests.get(url, proxies = proxx, timeout=timeoutk)
            print("FOUND")
            que.append(proxy)
        except:
            pass


def threads(arg, timeout):
    output = []
    threads = []
    a = arg.split()
    k = int(os.cpu_count()-2)
    chunks = [a[int(x):int(x+int(len(a))/k)] for x in range(0, len(a), int(len(a)/k))]
    for i in range(os.cpu_count()-2):
        threads.append(Thread(target=check, args=["\n".join(chunks[i]), output, timeout]))
    for thread in threads:
        print(thread, "started")
        thread.start()
    for thread in threads:
        thread.join()
    return "\n".join(output)

dicct = {"(Seven6ZeroNine^Four0Eight)" : "8",
"(Zero8TwoFour^Six5Nine)" : "0",
"(SixSixEightFive^Six3Three)" : "4",
"(Six1FiveThree^ThreeFourSeven)" : "6",
"(Two3SevenZero^NineSevenFive)" : "7",
"(NineTwoNineOne^EightTwoOne)" : "9",
"(ZeroFourFiveThree^Five5Three)" : "3",
"(SevenTwoEightEight^NineOneZero)" : "1",
"(SevenSevenSevenSeven^SevenThreeFour)" : "2",
"(FourZeroSixFour^Three8Eight)" : "5"}



#	Domain	Monthly traffic
theweb = ["https://www.youtube.com",
"https://www.en.wikipedia.org",
"https://www.twitter.com",
"https://www.facebook.com",
"https://www.amazon.com",
"https://www.yelp.com",
"https://www.reddit.com",
"https://www.imdb.com",
"https://www.fandom.com",
"https://www.pinterest.com",
"https://www.tripadvisor.com",
"https://www.instagram.com",
"https://www.walmart.com",
"https://www.craigslist.org",
"https://www.ebay.com",
"https://www.linkedin.com",
"https://www.play.google.com",
"https://www.healthline.com",
"https://www.etsy.com",
"https://www.indeed.com",
"https://www.apple.com",
"https://www.espn.com",
"https://www.webmd.com",
"https://www.fb.com",
"https://www.nytimes.com",
"https://www.google.com",
"https://www.cnn.com",
"https://www.merriam-webster.com",
"https://www.gamepedia.com",
"https://www.microsoft.com",
"https://www.target.com",
"https://www.homedepot.com",
"https://www.quora.com",
"https://www.nih.gov",
"https://www.rottentomatoes.com",
"https://www.netflix.com",
"https://www.quizlet.com",
"https://www.weather.com",
"https://www.mapquest.com",
"https://www.britannica.com",
"https://www.businessinsider.com",
"https://www.dictionary.com",
"https://www.zillow.com",
"https://www.mayoclinic.org",
"https://www.bestbuy.com",
"https://www.theguardian.com",
"https://www.yahoo.com",
"https://www.msn.com",
"https://www.usatoday.com",
"https://www.medicalnewstoday.com",
"https://www.urbandictionary.com",
"https://www.usnews.com",
"https://www.foxnews.com",
"https://www.genius.com",
"https://www.allrecipes.com",
"https://www.spotify.com",
"https://www.glassdoor.com",
"https://www.forbes.com",
"https://www.cnet.com",
"https://www.finance.yahoo.com",
"https://www.irs.gov",
"https://www.lowes.com",
"https://www.mail.yahoo.com",
"https://www.aol.com",
"https://www.steampowered.com",
"https://www.washingtonpost.com",
"https://www.usps.com",
"https://www.office.com",
"https://www.retailmenot.com",
"https://www.wiktionary.org",
"https://www.paypal.com",
"https://www.foodnetwork.com",
"https://www.hulu.com",
"https://www.live.com",
"https://www.cbssports.com",
"https://www.wayfair.com",
"https://www.ca.gov",
"https://www.bleacherreport.com",
"https://www.macys.com",
"https://www.accuweather.com",
"https://www.xfinity.com",
"https://www.go.com",
"https://www.techradar.com",
"https://www.groupon.com",
"https://www.investopedia.com",
"https://www.yellowpages.com",
"https://www.steamcommunity.com",
"https://www.chase.com",
"https://www.wellsfargo.com",
"https://www.npr.org",
"https://www.apartments.com",
"https://www.roblox.com",
"https://www.huffpost.com",
"https://www.books.google.com",
"https://www.bankofamerica.com",
"https://www.bbb.org",
"https://www.expedia.com",
"https://www.wikihow.com",
"https://www.ign.com",
"https://www.wowhead.com"]
