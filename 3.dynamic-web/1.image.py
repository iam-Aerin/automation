from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import requests

# 검색어 입력
keyword = input("검색어를 입력하세요: ")

# 웹드라이버 실행
driver = webdriver.Chrome()
time.sleep(2)

# 네이버 이미지 검색 접속
driver.get(f'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={keyword}')
time.sleep(2)

# 저장 폴더 생성
img_dir = f'./{keyword}'
if not os.path.exists(img_dir):
    os.makedirs(img_dir)

# 이미지 선택자 수정
imgs = driver.find_elements(By.CSS_SELECTOR, 'img._fe_image_tab_content_thumbnail_image')
img_list = []

for img in imgs:
    src = img.get_attribute('src')
    if src and src.startswith('http'):
        img_list.append(src)

# 최대 5개로 제한
img_list = img_list[:5]
print(f'{len(img_list)}개의 이미지 링크 수집됨')

# 이미지 다운로드
for i, src in enumerate(img_list, start=1):
    save_path = os.path.join(img_dir, str(i).zfill(3) + '.jpg')
    print(f'{save_path} 저장중...')

    headers = {
        'Referer': 'https://search.naver.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    try:
        img_data = requests.get(src, headers=headers).content
        with open(save_path, 'wb') as f:
            f.write(img_data)
            print('저장 완료')
    except Exception as e:
        print(f'다운로드 실패: {e}')
    
    time.sleep(1)
