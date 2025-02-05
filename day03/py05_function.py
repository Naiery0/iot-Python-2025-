# py05_function.py

# 함수, Function, Method, Procedure, ...동일
# 인자, parameter, 매개변수, Argument, ...동일
# def 함수명(인자, ...):
#   함수 안으로 진입
# def function(self)

def say_hi():
    print("안녕")
    return None

def say_hello(name):
    print(f'{name}야, 안녕')
    return None

def get_age(birthYear):
    age = 2025 - birthYear
    return age

def closing():
    return '빠잉'

say_hello(name = input('이름이 뭐야?'))

print('나이: 만',get_age(int(input('몇 년생이야?'))))

print(closing())    


# def sum(x,y,z):
#     result = x + y + z
#     return result

# print(sum(1,2,3))

