from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def SpyProxies():
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--remote-debugging-port=0")
    url = "http://spys.one/en/free-proxy-list/"
    a = webdriver.Chrome(options=chrome_options)
    a.get(url)
    show = Select(a.find_element_by_name("xpp"))

    while 1:
        try: 
            show.select_by_visible_text("500")
            show = Select(a.find_element_by_name("xpp"))
            k = show.first_selected_option
            print(k.text)
            if k.text == "500":
                break
            else:
                print("NOT")
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
    return "\n".join(result)

def get_proxy3():
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--remote-debugging-port=0")
    url = "https://www.proxy-list.download/HTTP"
    a = webdriver.Chrome(options=chrome_options)
    a.get(url)
    soup = a.find_element_by_id("txta1")
    kk = soup.get_attribute("value")
    a.quit()
    return kk


