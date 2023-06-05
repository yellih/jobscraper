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

def get_page_count(keyword):
    search_url = "https://kr.indeed.com/jobs?q="
    if get(f"{search_url}{keyword}").status_code == 200:
        print("Request Success!")
    else:
        browser.get(f"{search_url}{keyword}")
        soup = BeautifulSoup(browser.page_source, "html.parser")
        pagination = soup.find('nav', class_="css-jbuxu0")
        if pagination == None:
            return 1
        pages = pagination.find_all("div", class_="css-tvvxwd")
        count = len(pages)
        if count >= 5:
            return 5
        else:
            count

# print(get_page_count("python"))   

def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found",pages,"pages")
    results = []
    for page in range(pages):
        home_url = "https://kr.indeed.com"
        search_url = "https://kr.indeed.com/jobs"
        final_url = f"{search_url}?q={keyword}&start={page*10}"
        print("Requesting", final_url)
        if get(final_url).status_code == 200:
            print("Request Success!")
        else:
            browser.get(final_url)
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
                            'position': title.strip("의 전체 세부 정보")
                        }
                        results.append(job_data)
                # for result in results:
                #     print(result, "\n//\n//")
    return results

# jobs = extract_indeed_jobs("python")

# print(jobs)