import json
import requests
from bs4 import BeautifulSoup
from flask import request
import datetime


def get_weather():
    url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    output = ""

    for loc in soup.select("location"):
        output += f"<h3>{loc.select_one('city').string}<h3>"
        output += f"날씨 : {loc.select_one('wf').string}</br>"
        output += f"최저/최고 기온 : {loc.select_one('tmn').string}/{loc.select_one('tmx').string}</br>"

    return output

def get_weather2():
    print("GET 요청을 받았습니다.")
    nx_val = request.args.get('x')
    ny_val = request.args.get('y')
    print("X : ", nx_val)
    print("Y : ", ny_val)
    API_KEY = 'NOGPQxxLHIV58JR0gA3UDyOBxOhn3yTsYT2j0uPhRbmUa3l7M48i4GkQoAnMO%2Fyb38CrH9mqGrTvlU5bw4uyyg%3D%3D'
    API_KEY_decode = requests.utils.unquote(API_KEY)

    # 날짜 및 시간 설정
    now = datetime.datetime.now()

    # base_date에 날짜를 입력하기 위해 날짜를 출력 형식을 지정해 변수에 할당
    date = now.strftime('%Y%m%d')

    # base_time에 시간을 입력하기 위해 시간을 출력 형식을 지정해 변수에 할당
    time = now.strftime('%H%M')

    # 현재 분이 30분 이전이면 30분 전 시간으로 설정
    if now.minute < 30:
        now = now - datetime.timedelta(minutes=30)
        time = now.strftime('%H%M')
    else:
        time = now.strftime('%H%M')

    # 요청 주소 및 요청 변수 지정
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'

    # 발표 일자 지정
    baseDate = date
    baseTime = time

    # 한 페이지에 포함된 결과 수
    num_of_rows = 10
    # 페이지 번호
    page_no = 1
    # 응답 데이터 형식 지정
    data_type = 'JSON'

    req_parameter = {'serviceKey': API_KEY_decode,
                     'nx': nx_val, 'ny': ny_val,
                     'base_date': baseDate, 'base_time': baseTime,
                     'pageNo': page_no, 'numOfRows': num_of_rows,
                     'dataType': data_type}

    # 요청 및 응답
    try:
        r = requests.get(url, params=req_parameter)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making a request: {e}")
        return json.dumps({"error": str(e)}, ensure_ascii=False)

    # JSON 형태로 응답받은 데이터를 딕셔너리로 변환
    dict_data = r.json()

    # 출력을 이쁘게 하기 위해 json.dumps()를 사용하여 들여쓰기(indent) 옵션을 지정
    print(json.dumps(dict_data, indent=2))

    # 딕셔너리 데이터를 분석하여 원하는 데이터를 추출
    weather_items = dict_data['response']['body']['items']['item']

    print(f"[ 발표 날짜 : {weather_items[0]['baseDate']} ]")
    print(f"[ 발표 시간 : {weather_items[0]['baseTime']} ]")

    weather_data = {}

    def map_sky_code(sky_code):
        if sky_code == '1':
            return "맑음"
        elif sky_code == '3':
            return "구름 많음"
        elif sky_code == '4':
            return "흐림"
        else : return "알 수 없음"

    for k in range(len(weather_items)):
        weather_item = weather_items[k]
        fcstValue = weather_item['fcstValue']

        if weather_item['category'] == 'TMP': # 기온
            weather_data['tmp'] = f"{fcstValue}℃"
        elif weather_item['category'] == 'REH': # 습도
            weather_data['hum'] = f"{fcstValue}%"
        elif weather_item['category'] == 'PTY': # 강수 형태
            weather_data['pty'] = f"{fcstValue}"
            # 만약 sky 코드가 알 수 없음 이라면 pty 상태에 따라 처리
            if weather_data.get('sky') == "알 수 없음":
                if weather_data.get('sky') == "알 수 없음":
                    if fcstValue == '0':
                        weather_data['pty'] = "없음"
                    elif fcstValue == '1':
                        weather_data['pty'] = "비"
                    elif fcstValue == '2':
                        weather_data['pty'] = "비/눈"
                    elif fcstValue == '3':
                        weather_data['pty'] = "눈"
                    elif fcstValue == '4':
                        weather_data['pty'] = "소나기"
                weather_data['pty'] = f"{fcstValue}"
        elif weather_item['category'] == 'SKY':  # 하늘 상태
            weather_data['sky'] = map_sky_code(fcstValue)

    # 딕셔너리를 JSON 형태로 변환, # ensure_ascii=False를 설정하여 JSON에 유니코드 문자 포함
    json_weather = json.dumps(weather_data, ensure_ascii=False, indent=4)
    return json_weather