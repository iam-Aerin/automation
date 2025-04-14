from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()

URL = 'https://www.melon.com/chart/index.htm'
driver.get(URL)

song_info = driver.find_elements(By.CSS_SELECTOR, 'a.btn.song_info')
# print(song_info.get_attribute('title'))
# print(len(song_info))

song_list = []

for i in range(10): 
    song_info[i].click()
    time.sleep(2)
    
    title = driver.find_element(By.CSS_SELECTOR, 'div.song_name').text
    # print(title)
    # artist = driver.find_element(By.CSS_SELECTOR, 'div.artist > a > span').text
    artist = driver.find_element(By.CSS_SELECTOR, 'div.artist span').text

    # index 접근으로 (여러 데이터 중) 하나의 데이터 텍스트를 출력하기
    # meta_data = driver.find_elements(By.CSS_SELECTOR, 'div.meta dd')    
    # print(title, artist, meta_data[1].text)
    
    # 발매일 정보를 특정
    publish_date = driver.find_element(By.CSS_SELECTOR, 'dl.list > dd:nth-of-type(2)').text
     
    like_cnt = driver.find_element(By.CSS_SELECTOR, 'span#d_like_count').text
    # like_cnt의 쉼표 빼기
    like_cnt = like_cnt.replace(',', '')
    # print(like_cnt)
    # print(publish_date)
    
    
    song_list.append([title, artist, publish_date, like_cnt])
    
    driver.back()
    # 뒤로가기 버튼을 클릭합니다.
    
# print(song_list)

local_file_path = '/home/ubuntu/damf2/data/melon/'

def save_to_csv(song_list):
# 저장하는 코드를 함수화
    with open(local_file_path + 'melon-top-100.csv', 'w', encoding='utf-8') as file:
    # 시간별로 저장하고 싶다면 datetime 연결해서 활용 가능
        writer = csv.writer(file)
        writer.writerows(song_list)

save_to_csv(song_list)