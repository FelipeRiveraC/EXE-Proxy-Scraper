import os
import queue
import socket
import urllib
from random import choice
from threading import Thread

import requests
from bs4 import BeautifulSoup

def get_proxy(listn):
    url = "https://free-proxy-list.net/"
    a = requests.get(url)
    soup = BeautifulSoup(a.text, "html.parser")
    find = soup.find("div", id="raw")
    k = find.text.split()
    for i in range(11):
        del k[0]
    for i in k:
        listn.append(i)
    print(len(listn))

def get_proxy22(listn):
    url = "http://www.httptunnel.ge/ProxyListForFree.aspx"
    a = requests.get(url)
    soup = BeautifulSoup(a.text, "html.parser")
    find = soup.find_all("a")#, id="ctl00_ContentPlaceHolder1_GridViewNEW_ctl02_HyperLink2")
    for i in find:
        listn.append(i)

get_proxy22([])

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
