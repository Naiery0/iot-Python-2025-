# 리스트 이전
a = 1
b = 2
c = 3
d = 4
e = 5

sum = a + b + c + d + e
print(sum)

# 리스트(배열) 사용 - 다른 언어에선 리스트와 배열은 다른 개념
f = [1, 2, 3, 4, 5]
print(f)
print(type(f))

f = ['Life', 'is', True, 0, None, [1, 2, 3]]
print(f)
print(f[0])

# 리스트의 한 요소에도 값을 집어넣을 수 있다
f[3] = 100
print(f)

## 튜플
# 리스트와 거의 흡사. "값을 변경할 수 없음"
t = (1, 2, 3, 4)
print(t)
# t[0] = 5 -> 'tuple' object does not support item assignment 에러 발생
# tip : 주석 토글 'Ctrl + /'
print(type(t))

## 딕셔너리(사전형) {key : value}의 집합
spiderman = { 'name': 'Peter Parker', 'age': 20, 'weapon': 'Web Shooter'}
print(spiderman)
print(type(spiderman))

print(spiderman['name'])
spiderman['age'] = 21
print(spiderman)

## 집합 (), {}, [] 모두 사용 가능, 중복제거
s = set([1, 2, 3])
print(s)
print(type(s))

s = set('Hello World')
print(s) #리스트처럼 인덱스가 없다

## 변수명 지정 방식
## 의미있는 단어들의 조합으로 만들 것
phoneNumber = '010-6688-7733'
salaryBankAccount = '866-12-335566'

sum = ''
sum1 = ''
# 1sum = '' -> error 숫자로 시작 x
_sum = ''
sum_ = ''
# sum! = '' -> error 언더바 이외 특수문자 x
# sum-app = '' -> 연산자 x
