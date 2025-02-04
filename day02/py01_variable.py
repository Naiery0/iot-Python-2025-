# 변수와 자료형
# 변수는 => 변하는 수(Variable) <-> 상수(Constant)
# 상수 예 Pi = 3.14158265727

# 변수
a = None    # 특수형, None 타입
print(a)    # a라는 변수에 무슨 값이 들어있는지 콘솔에 출력
print(type(a))

a = 10  # 정수, Integer
print(a)    # 함수는 늘 괄호를 같이 사용
print(type(a))

a = 12.34   # 실수, Float
print(a)
print(type(a))

a = 0b11111110  # 2진수, Binary
print(a)
print(type(a))

a = 0xFE    # 16진수, Hex
print(a)
print(type(a))

a = 1_900_000_000   # 천단위마다 쉼표와 같이 표현(팁)
print(a)
print(type(a))

a = "Life is short, You need Python"    # 문자열, String
print(a)
print(type(a))

a = "Life is short, You need Python"    # 문자열
print(a)
print(type(a))

a = (3 > 1) # boolean형
print(a)
print(type(a))