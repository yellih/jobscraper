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

home_url = "https://kr.indeed.com"
search_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

if get(f"{search_url}{search_term}").status_code == 200:
    print("Request Success!")
else:
    results = []
    browser.get(f"{search_url}{search_term}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    if soup.find("ul", class_="jobsearch-ResultsList") == None:
        print("Traffic alert is working, You need to wait")
    else:
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        # print(job_list)
        jobs = job_list.find_all("li", recursive=False)
        # print(len(jobs))
        for job in jobs:
            zone = job.find("div",class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                # print(anchor)
                # print("//")
                title = anchor['aria-label']
                link = anchor['href']
                # print(title, link)
                # print("//")
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                    'link':home_url+link,
                    'company': company.string,
                    'location': location.string,
                    'position': title
                }
                results.append(job_data)
        for result in results:
            print(result, "\n//\n//")