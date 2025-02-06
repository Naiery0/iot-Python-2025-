# py01_list_op.py

# 리스트연산
# 리스트가 for, while 반복문에서 가장 많이 활용되는 구조
# iterable -> 반복할 수 있는 요소가 for, while문에 사용
listSample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
sum = 0
for i in listSample:
    sum = sum + i

print(f'합산결과 = {sum}')

arr = [1, 2, 3, 4, 5]
arr2= [6, 7, 8, 9, 0]
print(arr)
print(arr[1])
print(arr[0] + arr[2])
print(arr[-1])

print(arr[2:])

# 문자열 연산과 같은 원리
print(arr + arr2)
print(arr * 2) 


## 리스트 길이
print(len(arr))

# 데이터 할당
arr[2] = 9
print(arr)

# 리스트 요소 삭제
arr[2] = None
print(len(arr))
del(arr[2])
print(len(arr))

# 리스트 요소 추가
arr.append(7) # 리스트 마지막에 추가
print(arr)
arr.insert(0, 100) # 0번 인덱스에 100 삽입 
print(arr)

## 리스트 병합 시
print(arr.extend(arr2))

## 리스트 정렬
arr = [6, 7, 1, 3, 9, 0, 2, 8]
arr.sort()  # 오름차순 정렬
print(arr)
arr.sort(reverse=1)
print(arr)

## 요소의 위치 파악
print(arr.index(3))

## 요소 꺼내기
print(arr.pop()) # 마지막 요소가 꺼내짐
print(arr)

## 리스트 컴프리핸션
arr = [i for i in range(1, 100 + 1)]
print(arr)

sum = 0
for i in arr:
    sum = sum + i

print(f'{len(arr)}까지의 합산은, {sum}입니다.')
