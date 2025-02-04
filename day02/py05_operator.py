# py05_operator.py
# 연산자

# 사칙연산 +, -, *, /
a, b = 5, 3
# tip : Shift + Del -> 한줄 삭제

print(a + b)
print(a - b)
print(a * b)

# 나누기 /, //, %
print(a / b) # 나눈 결과는 float
print(a // b) # 몫 int 
print(a % b) # 나머지 int

# 거듭제곱(Power) **
print(2 ** 5)

# 연산자 우선순위
## 계산식이 복잡하여 우선순위를 모르겠으면 ()
print((3 + 4) * 7)
print(3 + (4 * 7))

## 리스트연산
## last index = len(list)-1
listSample = [1, 3, 5, 7, 9]
print(listSample[0])
print(len(listSample)) # 리스트의 길이

print(listSample[1])
print(listSample[2])
print(listSample[3])
print(listSample[4])
print(listSample[len(listSample)-1])

## 문자열 연산
greeting = 'Hello'
target = 'world'
print(greeting, target)

print(greeting + target) # string concatenate
print('{0} {1}'.format(greeting, target))
print(f'{greeting} {target}')

print(greeting * 5) # 해당 문자열을 * 수로 반복

listSample = ['2','0','2','5','-','0','2','-','0','4']
current = '2025-02-04'

# 슬라이싱, 리스트를 자르기
print(listSample[0:3]) # 인덱스 3번 앞까지만. (0~2번까지 출력)


# 2025-02-04
year = current[0:3 + 1]
month = current[5:6 + 1]
day = current[8:] # 끝까지
print (year, month, day)

## 문자열 연산 중 함수 사용
full_name = "Hugo Mg. Sung"
# 자르기
print(full_name.split())
print(full_name.split(' '))

names = full_name.split(' ')
print(type(names))
print(names)

names = full_name.split('.')
print(type(names))
print(names)

# 바꾸기
print(full_name.replace('Hugo', 'Ashley'))

# 공백제거
origin = '     hello  ~     '
print(f'//{origin.lstrip()}//') # 좌 공백제거
print(f'//{origin.rstrip()}//') # 우 공백제거
print(f'//{origin.strip()}//') # 좌우 공백제거

# 단어찾기
full_name = "Hugo Mg. Sung"
print(full_name.find('g')) # 찾은 첫 번째 인덱스, 없으면 -1 출력
print(full_name.count('g')) # g가 문장에 몇 개 존재하는가?
#print(full_name.index('h')) # 오류 남.
print(full_name.upper()) #대문자
print(full_name.lower()) #소문자