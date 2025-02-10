# py06_exception.py

# 예외처리
## 오류, Error, Fault, ...
## 1. Error(문법적 오류) - 코딩하다가 빨간 밑줄
##      오류 검출이 안 되는 단순 실수로 인한 논리 오류
## 2. Exception(실행 중 발생하는 예외) - 문법 오류x 실행 중 비정상 종료되는 상황
## 파이썬은 Error도 Exception도 Error라고 보여줌
## 에디터 상에 오류표시가 나면 Error
## 실행 중에 발생하면 Exception
# 디버깅 - 천천히 어디에서 예외가 발생하는가?
## f9 - 중단점 표시 해제 가능
## f5 - 디버깅 시작, 중단점까지
## f10 - 한줄 실행, 함수 있어도 함수를 실행하고 넘어감
## f11 = 한줄 실행, 함수가 있으면 함수 안으로 진입
## shift + f5 - 디버깅 종료
## 변수 탭 - 현재 변수에 들어있는 값 표시
## 조사식 탭 - 내가 원하는 식을 실행한 결과
## Exception 클래스는 모든 예외 클래스의 조상
## try문을 반복해서 사용하면 속도 저하의 원인이 됨

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
            try:
                x, y = input('곱할 수 입력 > ').split()
                x = int(x)
                y = int(y)
                print(f'{x} * {y} = {mul(x, y)}')
            except ValueError as e: # ValueError 클래스에 대한 e 객체 생성됨 
                print(f'다시 하세요 {e}')

            # break
        elif op == '/':
            try:
                x, y = input('나눌 수 입력 > ').split()
                x = int(x)
                y = int(y)
                print(f'{x} / {y} = {div(x, y)}')
            except Exception as e:
                print(f'{e}')
            
            # except ValueError as e: # ValueError 클래스에 대한 e 객체 생성됨 
            #     print(f'다시 하세요 {e}')
            
            # # 0으로 나누면 ValueError가 못 잡음 (Zero division)
            # except ZeroDivisionError as e:
            #     print('0으로 나눌 수 없습니다.')
            #     print(f'{e}')
            # break 
        else:
            print('정확한 입력 요망')
            
    # except: print('정확한 입력 요망')

        