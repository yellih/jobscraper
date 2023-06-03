'weworkremotely(https://weworkremotely.com/)' 및 'indeed(https://kr.indeed.com/)' 두가지 홈페이지에 접속하여
게시글링크, 회사명, 지역, 직책을 가져옴

BeautifulSoup과 Selenium을 이용하여 작성함

weworkremotely는 홈페이지 UI가 자주 바뀌에서 DOM(css selector)가 바뀌면 코드가 작동하지 않는 단점이 있음

indeed는 봇을 막는 기능이 있어 requests의 get으로 url에 접속하여 추출하지 못 하므로 Selenium을 써서 브라우저가 열리는 방식으로 동작하게 함

selenium의 브라우저가 자동으로 닫히기 때문에 Service와 ChromeDriverManager를 import함

selenium의 브라우저를 열어놓을 필요 없이 자동으로 닫힌 상태에서도 추출이 되긴 하지만, 브라우저가 자동으로 닫히는채로 두고 작동하면 데이터 추출이 되지 않을 때 봇 막는 페이지가 작동해서 안되는 건지 뭔지 확인할 수가 없기 때문에 브라우저가 닫히지 않게 함

weworkremotely 스크린샷 1 (2023.06.03)
![screencapture-weworkremotely-remote-jobs-search-2023-06-03-12_49_01](https://github.com/yellih/jobscraper/assets/127484092/147b03ad-d1fa-40a5-bf38-aa4ea06f99e5)

weworkremotely 스크린샷 2 (2023.06.03)
![screencapture-weworkremotely-categories-remote-back-end-programming-jobs-2023-06-03-12_49_25](https://github.com/yellih/jobscraper/assets/127484092/fb1788c2-908e-47fb-b1d1-acadd85c527f)

indeed 스크린샷 (2023.06.03)
![screencapture-kr-indeed-jobs-2023-06-03-12_52_02](https://github.com/yellih/jobscraper/assets/127484092/b904bf6c-fc42-47d0-8489-433983d06681)

출처 노마드코더 - Python으로 웹 스크래퍼 만들기 (https://nomadcoders.co/python-for-beginners/lobby)
