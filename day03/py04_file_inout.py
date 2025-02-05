# py04_file_input.py

# 파일 입출력
# 오픈 읽고 쓰고 닫기
# 파일 경로 중요
# mode: 읽기 r, 쓰기 w, 추가 a, ...
# encoding: 한글만(euc-kr, cp949), 국제어(utf-8)
# 파일 경로 구분은 /, \ 둘 다 가능, '\'는 문자열에서 표현하기 위해 '\\' 라고 써야 함

## 상대경로 - 경로를 특수문자로 생략
# .: 현재 자기 위치 (iot_python_2025_)
# ..: 자신의 부모 폴더 위치
# f = open('./day03/test.txt', mode = 'w', encoding = 'utf-8')

## 절대경로 - 드라이브부터 모든 경로 기재
f = open('C:/source/iot-python-2025-/day03/test.txt', mode = 'w', encoding = 'utf-8')

f.write('파일 쓰기 시작!')
f.write('\n두 번째 줄 작성합니다.\n')


f.close()

print('파일 쓰기 완료')

r = open('./day03/test.txt', mode = 'r', encoding = 'utf-8')

while 1 :
    line = r.readline() # 한 줄씩 읽음
    if not line: # 한 줄을 읽은 값이 None이라면
        break # while문 탈출
    
    # \n 없애기
    print(line, end='')
    # print(line.replace('\n', ''))
    

r.close()


