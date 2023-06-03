'weworkremotely(https://weworkremotely.com/)' 및 'indeed(https://kr.indeed.com/)' 두가지 홈페이지에 접속하여
게시글링크, 회사명, 지역, 직책을 가져옴

BeautifulSoup과 Selenium을 이용하여 작성함

weworkremotely는 홈페이지 UI가 자주 바뀌에서 DOM(css selector)가 바뀌면 코드가 작동하지 않는 단점이 있음

indeed는 봇을 막는 기능이 있어 requests의 get으로 url에 접속하여 추출하지 못 하므로 Selenium을 써서 브라우저가 열리는 방식으로 동작하게 함
