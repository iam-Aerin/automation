from datetime import datetime
import requests
import time
import csv

upbit_url = 'https://api.upbit.com/v1/ticker?markets=KRW-BTC'

start_time = time.time()

bit_data_list = []

while time.time() - start_time < 60:
    # 최신 시간 - 과거의 (데이터를 활성화했던) 시간 < 1분이전
    
    res = requests.get(upbit_url)
#json 형식을 dictionary 형태의 데이터로 변환
    data = res.json()[0]
    
    # 내가 필요한 데이터 몇개만 리스트로 변환
    bit_data = [
        data['market'], data['trade_date'],data['trade_time'], data['trade_price']]
    bit_data_list.append(bit_data)
    time.sleep(15)
    
# 만들어진 리스트 (데이터)를 파일로 저장
# ubuntu@smart:~/damf2/data$ mkdir bitcoin 폴더 생성
# data폴더 안에 bitcoin폴더 생성

# 파일 경로를 변수로 지정
local_file_path = '/home/ubuntu/damf2/data/bitcoin/'

# 이 위치에 파일을 생성할 수 있도록 코드
# 현재 시간의 데이터를 가져와서, 그걸 파일 이름에 적용하도록
now = datetime.now()
file_name = now.strftime('%H-%M-%S') + '.csv'

# 파일 저장하기
with open(local_file_path + file_name, mode='w', newline='') as file:
    # 내가 연 파일을 파일이라는 변수에 저장
    # with 내에서만 file이라는 변수를 사용하겠다. 
    
    # mode='w' : 파일을 쓰기 모드로 열어줌
    # newline='' : 엔터키를 입력하면 자동으로 줄바꿈을 해줌
    
    # open이라는 함수의 역할은?
    # 파일을 열고, 파일을 쓸 수 있는 상태로 만들어주는 역할
    writer = csv.writer(file)
    # 파일 열기
    # csv모듈이 가지고 있는 함수, csv.writer()
    writer.writerows(bit_data_list)
    # 파일에 쓰기
    