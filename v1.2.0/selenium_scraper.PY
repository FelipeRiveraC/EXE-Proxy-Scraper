from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def SpyProxies(senal):
    useragen = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--remote-debugging-port=0")
    chrome_options.add_argument(f"User-Agent={useragen}")
    url = "http://spys.one/en/free-proxy-list/"


    a = webdriver.Chrome(options=chrome_options)
    a.get(url)
    show = Select(a.find_element_by_name("xpp"))

    while 1:
        try: 
            show.select_by_visible_text("500")
            show = Select(a.find_element_by_name("xpp"))
            k = show.first_selected_option
            if k.text == "500":
                break
            else:
                pass
        except: pass


    while 1:
        soupt = BeautifulSoup(a.page_source, "html.parser")
        find1t = soupt.find_all("font", class_="spy14")
        if len(find1t) > 300:
            break

    soup = BeautifulSoup(a.page_source, "html.parser")
    find1 = soup.find_all("font", class_="spy14")
    result = [i.text for i in find1 if i.text.count(".") ==3 and i.text.count(":") == 1]
    a.quit()

    for i in result:
        if i[0].isnumeric() and i.count(".") == 3:
            senal.emit(i + "\n")


def get_proxy3(listn, senal):
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--remote-debugging-port=0")
    url = "https://www.proxy-list.download/HTTP"
    a = webdriver.Chrome(options=chrome_options)
    a.get(url)
    sleep(2)
    soup = a.find_element_by_id("txta1")
    kk = soup.get_attribute("value")
    a.quit()
    bbb = str(kk).split()
    for i in bbb:
        if i[0].isnumeric() and i.count(".") == 3:
            senal.emit(i + "\n")

    return kk


def get_proxy4(senal):
    useragen = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    k, c = [], True
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"User-Agent={useragen}")
    chrome_options.add_argument("--remote-debugging-port=0")
    url = ["https://hidemy.name/en/proxy-list/", "https://hidemy.name/en/proxy-list/?start=64#list", "https://hidemy.name/en/proxy-list/?start=128#list", "https://hidemy.name/en/proxy-list/?start=192#list", "https://hidemy.name/en/proxy-list/?start=256#list", "https://hidemy.name/en/proxy-list/?start=320#list", "https://hidemy.name/en/proxy-list/?start=384#list", "https://hidemy.name/en/proxy-list/?start=448#list", "https://hidemy.name/en/proxy-list/?start=512#list", "https://hidemy.name/en/proxy-list/?start=576#list" ]
    a = webdriver.Chrome(options=chrome_options)
    for i in range(10):
        try:
            a.get(url[i])
            sleep(3)

            if c == True:
                sleep(8)
                c = False

            find = a.find_element_by_class_name("table_block")
            k = find.text.split()
            for element in k:
                if element.count(".") == 3:
                    #print(f"{element}:{k[k.index(element)+1]}")
                    senal.emit(f"{element}:{k[k.index(element)+1]}\n")
        except:
            print("ERROR")
            pass
    a.quit()