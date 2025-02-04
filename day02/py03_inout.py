# py03_inout.py
# 화면입출력

print('출력입니다.')

number = input('만나이를 입력하세요 > ') # 입력방법
# 입력값, 출력값 모두 문자열임
print(type(number)) # str 타입임
# print("현재 나이는 : ", number + 1) -> str에 연산은 불가능하기에 error 

number=int(number)
print(type(number)) # int 타입임
print("현재 나이는 : ", number + 1) # 여러 값 출력 ','

x, y = input('합산할 두 수를 입력하쇼').split() # (기본은 공백으로) 자른다
x = int(x)
y = int(y)
print(x + y)