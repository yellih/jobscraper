from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  #브라우저 실행 후 자동 닫힘 방지1
from webdriver_manager.chrome import ChromeDriverManager  #브라우저 실행 후 자동 닫힘 방지2
from requests import get
from bs4 import BeautifulSoup

options = Options()
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches',['enable-longging'])

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service,options=options)

search_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

if get(f"{search_url}{search_term}").status_code == 200:
    print("Request Success!")
else:
    browser.get(f"{search_url}{search_term}")
    print(browser.page_source)