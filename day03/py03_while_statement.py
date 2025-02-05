# py03_while_statement.py

# while : for문으로 변경 가능

# 1~10 합산

sum, i = 0, 0

while i <= 10:
    sum += i
    i += 1  # +=, -=, *=, /=, ...

print(f'합은 {sum}')
sum = 0

for j in range(1, 10 + 1):
    sum += j
print(f'합은 {sum}')