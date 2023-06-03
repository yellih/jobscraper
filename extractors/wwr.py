from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):

    wwr_url = "https://weworkremotely.com"
    search_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
    view_all_url = ""
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
                view_all_url = link[0]['href']
                # print(view_all_url)
            
    view_all_url_response = get(f"{wwr_url}{view_all_url}")
    # print(f"{wwr_url}{view_all_url}")
    # print(view_all_url_response)

    if view_all_url_response.status_code != 200:
        print("Can't request website")
    else:
        results = []
        soup = BeautifulSoup(view_all_url_response.text, "html.parser")
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
                company, kind, region = anchor.find_all('span', class_="company")
                # print(company,kind, region)
                title = anchor.find('span', class_='title')
                job_data = {
                    'link':wwr_url+link,
                    'company': company.string,
                    'region': region.string,
                    'position': title.string
                }
                results.append(job_data)
        # print(results)
        return results