# py06_exception.py

# 예외처리
## 오류, Error, Fault, ...
## 1. Error(문법적 오류) - 코딩하다가 빨간 밑줄
##      오류 검출이 안 되는 단순 실수로 인한 논리 오류
## 2. Exception(실행 중 발생하는 예외) - 문법 오류x 실행 중 비정상 종료되는 상황
## 파이썬은 Error도 Exception도 Error라고 보여줌
## 에디터 상에 오류표시가 나면 Error
## 실행 중에 발생하면 Exception
numbers = list(range(1, 11))
for i in numbers:
    # print(i)
    pass

def mul(a, b):
    return a * b
def div(a, b):
    return a / b

print('계산 시작')
while 1:
    #try:
        op = input('계산할 연산을 입력(*, /, q)')
        if op == 'q':
            print('종료합니다.')
            break 
        elif op == '*':
            x, y = input('곱할 수 입력 > ').split()
            x = int(x)
            y = int(y)
            print(f'{x} * {y} = {mul(x, y)}')

            # break
        elif op == '/':
            x, y = input('나눌 수 입력 > ').split()
            x = int(x)
            y = int(y)
            print(f'{x} / {y} = {div(x, y)}')
            
            # break 
        else:
            print('정확한 입력 요망')
            
    # except: print('정확한 입력 요망')

        