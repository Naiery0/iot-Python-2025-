# py05_module.py

# pip install requests
# https://pypi.org 외부 패키지 사이트
import requests
print('외부 패키지 사용')

# 웹 브라우저가 아닌 파이썬 상에서 웹 접속
res = requests.get('https://www.google.com')

print(res.status_code)
# # print(res.content)
f = open('./day04/index.html', mode='w', encoding='utf-8')

f.write(str(res.content, 'utf-8'))
f.close()
print('파일 작성 완료')


class Sample:
    pass
import py02_car as c

## __main__ -> 프로그램이 시작하는 진입점(entry point)을 지칭
# C언어 등의 Static void main()와 동일한 역할
# 폴더 안에 py파일 중, 실행되는 파이썬 파일이 __main__ (진입점)
# 나머지는 모듈임.
if __name__ == '__main__':
    sam = Sample()
    print(sam)      # Sample 클래스가 메인
    print(__name__)
    car = c.Car()    # 모듈
    print(car)