# py01_if_statement.py
# if문: 흐름제어의 가장 기본
# if (조건이 참이면):
#    if문 안으로 들어간다!



# age = int(input('나이를 입력하세요.'))
# # age = int(age) 윗줄에 형변환 삽입

# # 만약 만 19세가 아니면
# # 조건이 여러 개일 때는 and, or로 더 가능
# if age >= 19 : # 참
#     print('4,500원입니다.')
# else : # 거짓
#     print ('집에 가라 ')


grade = input('학점을 입력하십시오.(A | B | C | D | F)')
while 1:
    if grade == 'A' or grade == 'B': # 이 구문에 걸리면
        # 구문 안으로 들어간다
        print('모범생')
        if grade == 'A': 
            print('장학금 줄게요')

        break
    elif grade == 'C' or grade == 'D':
        print('분발해')
        break
    elif grade == 'F':
        print('나가')
        break
    else: 
        grade = input('다시 입력하세요.')
