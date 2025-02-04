# 문자열 포맷팅 (포멧스트링)
# loginTemp = '안녕하세요, %s님!'
# name = '유고'

# print(loginTemp % (name))
# name = input('이름 입력 >')
# print (loginTemp % name)

## 구세대 문자열 포맷팅
intro = '나는 %s(이)고, %d살입니다. 몸무게는 %fkg입니다.'
print(intro % ('유고', 47, 60.0))

# %10s -> 무조건 10칸, %05d -> 5자리 중 남는 자리는 0으로, %.1f -> 소숫점 1자리까지만
intro = '나는 %10s(이)고, %05d살입니다. 몸무게는 %3.1fkg입니다.'
print(intro % ('유고', 47, 60.0))

## 중간세대 문자열 포맷팅 -> 입력 값 그대로 출력
intro = '나는 {0}이고, {1}살입니다. 몸무게는 {2}kg입니다.'
print(intro.format('육오', 48, 65.5))

#이런 식으로 꾸미기 가능
intro = '나는 {0:>10s}이고, {1}살입니다. 몸무게는 {2}kg입니다.'
print(intro.format('육오', 48, 65.5))

## 신세대 문자열 포맷팅
name = '유고잉'
age = 47
weight = 65.5
print(f'나는 {name:>10s}이고, {age}살입니다. 몸무게는 {weight}kg입니다.')