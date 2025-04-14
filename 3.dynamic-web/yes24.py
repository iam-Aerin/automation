from playwright.sync_api import sync_playwright
import getpass
import time
import random

# 사용자 입력 받기
user_id = input("YES24 아이디를 입력하세요: ")
user_pw = getpass.getpass("비밀번호를 입력하세요 (입력값은 표시되지 않습니다): ")

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-gpu",
        ]
    )

    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 800},
        locale="ko-KR"
    )

    page = context.new_page()

    # ✅ 메인 페이지 접속
    page.goto("https://ticket.yes24.com")
    time.sleep(random.uniform(1.5, 2.5))

    # ✅ 로그인 버튼 클릭 (사람처럼 마우스 이동 후 클릭)
    login_button = page.locator("#consiceLogin")
    box = login_button.bounding_box()
    page.mouse.move(box["x"] + 5, box["y"] + 5)
    page.mouse.click(box["x"] + 5, box["y"] + 5)
    time.sleep(random.uniform(1.2, 2.0))

    # ✅ ID/PW 입력 (사람처럼 타이핑)
    page.click("#SMemberID")
    for char in user_id:
        page.keyboard.insert_text(char)
        time.sleep(random.uniform(0.05, 0.15))

    page.click("#SMemberPassword")
    for char in user_pw:
        page.keyboard.insert_text(char)
        time.sleep(random.uniform(0.05, 0.15))

    page.keyboard.press("Enter")
    print("✅ 로그인 시도 중...")

    # ✅ 로그인 완료 대기
    page.wait_for_timeout(4000)

    # ✅ 스크린샷 저장
    page.screenshot(path="yes24_login_result.png")
    print("📸 로그인 결과 스크린샷 저장됨 (yes24_login_result.png)")
