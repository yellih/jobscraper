from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):

    home_url = "https://weworkremotely.com"
    search_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
    page_url = ""
    search_url_response = get(f"{search_url}{keyword}")

    if search_url_response.status_code != 200:
        print("Can't request website")
    else:
        soup = BeautifulSoup(search_url_response.text, "html.parser")
        section = soup.find_all('section',class_="jobs")
        # print(section[-1])
        for ul in section:
            view = ul.find_all('li',class_='view-all')
            # print(view)
            for li in view:
                link = li.find_all('a')
                page_url = link[0]['href']
                # print(page_url)
            
    page_url_response = get(f"{home_url}{page_url}")
    # print(f"{home_url}{page_url}")
    # print(page_url_response)

    if page_url_response.status_code != 200:
        print("Can't request website")
    else:
        results = []
        soup = BeautifulSoup(page_url_response.text, "html.parser")
        section = soup.find_all('section',class_="jobs")
        # print(section)
        for ul in section:
            li = ul.find_all('li')
            # print(li)
            # print(len(li))
            li.pop(-1)
            li.pop(0)
            # print(li)
            for post in li:
                anchors = post.find_all('a')
                # print(anchors)
                anchor = anchors[1]
                # print(anchor)
                link = anchor['href']
                # print(link)
                company, kind, location = anchor.find_all('span', class_="company")
                # print(company,kind, location)
                title = anchor.find('span', class_='title')
                job_data = {
                    'link':home_url+link,
                    'company': company.string,
                    'location': location.string,
                    'position': title.string
                }
                results.append(job_data)
        # print(results)
        return results