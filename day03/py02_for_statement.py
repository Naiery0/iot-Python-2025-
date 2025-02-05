# py02_for_statement.py

# for문
# for 변수 in 반복값:



## 아래와 같이 출력되는 프로그램
'''
최대 별 수: 4
*
**
***
****
'''

# range() 범위를 생성하는 클래스
# 마지막 수: max - 1
# range(8) == range(0, 8)
# range(초기값, 최대값, 증가값)
# print(range(8))

# for i in [0, 1, 2, 3, 4, 5, 6, 7]:
# for i in range(0, 8):
#     print(i)

# num = int(input('최대 별 수: '))

# for i in range(num): 
#     print('*' * (i + 1))
# # for i in range(1, num + 1): 
# #     print('*' * (i))

# 구구단 (이중 for문)
# 2 x 1 ~ 9 x 9

num = 9
for i in range(2, num + 1):
    if i == 7: continue
    for j in range(1, num + 1):
        # print(i, ' x ', j, '=', i * j)
        print(f'{i} x {j} = {i * j:2d}', end= '   ')
    print() # 한 줄 내리기

    #스트링포맷 더 공부 좀

## 반복문 탈출 break

