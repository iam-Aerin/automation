import requests
from bs4 import BeautifulSoup

lotto_url = 'https://dhlottery.co.kr/common.do?method=main'

res = requests.get(lotto_url)

soup = BeautifulSoup(res.text, 'html.parser')
# 내가 가진 데이터의 규격이 html임을 알려줌

# 내가 원하는 요소를 찾아주세요. 라는 bs4의 함수 기능을 이제 사용 할 수 있다. 
# soup.select()
balls = soup.select('span.ball_645')
for ball in balls:
    print(ball.text)