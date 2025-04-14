from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import os
import time

# 크롬 브라우저 옵션 설정
options = Options()
# options.add_argument('--headless')  # 필요 시 주석 해제
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)

# URL 접속
driver.get("https://kream.co.kr/?tab=home_ranking_v2")
time.sleep(3)

# 요소 로드될 때까지 대기
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.home-ranking-list__item--product"))
)

# 상위 10개 상품 추출
products = driver.find_elements(By.CSS_SELECTOR, "a.home-ranking-list__item--product")[:10]
print(f"총 상품 수: {len(products)}")

item_list = []

for product in products:
    try:
        name = product.find_element(
            By.CSS_SELECTOR,
            "p.text-lookup.text-product-name.display_paragraph.line_break_by_truncating_tail"
        ).text.strip()

        price = product.find_element(
            By.CSS_SELECTOR,
            "p.text-lookup.text-price.display_paragraph"
        ).text.strip()
        
        # 가격 정제: "106,000원" → 106000
        price = price.replace(",", "").replace("원", "")

        print(f"{name} / {price}")
        item_list.append([name, price])

    except Exception as e:
        print("❗️오류 발생:", e)

driver.quit()

# CSV 저장
save_dir = "/home/ubuntu/damf2/data/kream"
os.makedirs(save_dir, exist_ok=True)

with open(os.path.join(save_dir, "kream_top10.csv"), "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["상품명", "가격(원)"])
    writer.writerows(item_list)

print("✅ 크롤링 및 저장 완료")
