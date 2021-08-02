# 시퀀스 내장 함수
# enumerate() : 해당 요소와 인덱스가 튜플 형식으로 출력
'''
    <형식>
    for 인덱스번호, 값 in enumerate(리스트명) :
'''
a = [10, 20, 30]
for i in a:
    print(i)    # 리스트의 값만 출력

for item in enumerate(['가위', '바위', '보']):
    print(item)
print()

for index, value in enumerate(['가위', '바위', '보']): # unpacking
    print(index, value)
print()

for index, value in enumerate(a, start = 1): # unpacking
    print(f'{index}번째 : {value}')
print()

# len() : 객체 길이 또는 항목 수
li = ['a', 'b', 'c', 'd']
print(len(li))

d = {'a':'apple', 'b':'banana'}
print(len(d))

print(len(range(10)))   # 0 ~ 9
print(len(range(1, 10)))     # 1 ~ 9
print()

# sorted() : 오름차순 정렬
# reverse = True 옵션 추가 -> 내림차순
# reverse = False 옵션 추가 -> 오름차순
list1 = [6, 3, 1, 2, 7, 5, 4]
print(sorted(list1))
print()

# ex) 총점과 평균 구하기
score = [70, 65, 55, 75, 95]    # 학생 점수 리스트
total = 0

for i, v in enumerate(score, start = 1) :
    print(f'{i}번째 학생 점수 : {v}')
    total += v
print('총점 :', total)
avg = total // len(score)
print('평균 :', avg)
print()

# zip() : 튜플로 
names = ['james', 'David', 'Emily']
scores = [60, 70, 80]
for student in zip(names, scores):
    print(student)

print()

# p.g 159
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for month, day in enumerate(months):
    print(f'{month+1}월 = {day}일')

print()
