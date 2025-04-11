## 크롤링
> 일정 주기별로 원하는 정보를 가져오기
>
> 나중에 AIRFLOW로 더 간편하게 하는 방법이 있음

### 크롤링 방법
> 웹페이지를 크롤링하는 방법은 크게 2가지로 나눌 수 있다.
> 1. 브라우저를 이용한 크롤링
> 2. 웹 스크래퍼를 이용한 크롤링

#### 브라우저를 이용한 크롤링
> 브라우저를 이용해서 웹페이지를 크롤링하는 방법은 크게 2가지로 나눌 수 있다.
> 1. 웹페이지를 직접 열어서 크롤------------------
---
https://github.com/pyenv/pyenv?tab=readme-ov-file#installation
> `python 설치`

`source venv/bin/activate`: 리눅스에서 가상환경 (venv) 활성화

## Cron
> Job scheduler
: 유닉스 컴퓨터 운영 체제의 시간 기반 잡 스케줄러
: 5개의 주기로 구성: 분, 시, 월, 년, 주, 요일

### 크론 잡 등록
cron job scheduling



```shell
crontab -e
```
/home/ubuntu/damf2/automation/venv/bin/python

5 * * * * * /home/ubuntu/damf2/automation/venv/bin/python /home/ubuntu/damf2/autonmation/0.log/0.log_generate.py
- insert문 나가는 방법: `esc` + `:wq`

## cron 리스트 확인

```shell
crontab -l
```
