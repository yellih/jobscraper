from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"

response = get(f"{base_url}{search_term}")


soup = BeautifulSoup(response.text, "html.parser")
section = soup.find_all('section',class_="jobs")
for ul in section:
    view = ul.find_all('li' > 'a')
    print(view[-1]['href'])