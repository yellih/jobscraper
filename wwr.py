from requests import get
from bs4 import BeautifulSoup

wwr_url = "https://weworkremotely.com/"
search_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"
view_all_url = ""

search_url_response = get(f"{search_url}{search_term}")

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
# print(view_all_url_response)

if view_all_url_response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(view_all_url_response.text, "html.parser")
    section = soup.find_all('section',class_="jobs")
    # print(section2)
    for ul in section:
        li = ul.find_all('li')
        # print(li)
        # print(len(li))
        li.pop(-1)
        for post in li:
            anchors = post.find_all('a')
            # print(anchors)
            anchor = anchors[1]
            link = anchor['href']
            # print(anchor)
            company, kind, region = anchor.find_all('span', class_="company")
            # print(company,kind, region)
            title = anchor.find('span', class_='title')
            print(company,kind, region, title)
            print('//')