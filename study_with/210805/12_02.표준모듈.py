# 표준 모듈
# math 모듈

import math

print(math.pi)  # 원주율
print(math.ceil(1.1))   # 올림
print(math.floor(1.1))  # 내림

print(math.trunc(-1.9)) # 버림
print(math.floor(-1.9)) # -1.9보다 작은 정수로 내림

print(math.sqrt(25))    # 제곱근

print(math.pow(2, 3))   # 2의 3승

print()

# random 모듈
import random

print(random.randint(1, 10))    # 1이상 10 이하의 정수 중 아무 숫자
print()

print(random.randrange(10))     # 0 ~ 9 수 중 아무 숫자
print(random.randrange(1, 10))     # 1 ~ 9 수 중 아무 숫자
print(random.randrange(1, 10, 2))  # 1, 3, 5, 7, 9 수 중 아무 숫자
print()

print(random.random())  # 0 이상 1 미만 중
print()

seasons = ['spring', 'summer', 'fall', 'winter']
print(random.choice(seasons))   # seasons 리스트 값 중 하나
print()

print(random.sample(range(1, 46), 6))   # 1 ~ 45 중복 없이 6개 숫자 리스트 자료형으로 추출
print()

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)     # 임의로 섞기
print(my_list)
print()

# ex) 랜덤 모듈을 이용해서 무작위로 덧셈 문제를 만들어 맞추기
import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

print(f'{num1} + {num2} = ??')  # 문제 부분
ans = int(input('정답은 무엇입니까?? '))    # 정답 입력

if num1 + num2 == ans:
    print('정답입니다!')
else :
    print('오답입니다.')

print()
    
# p.g 213
import random

dice = random.randint(1, 6)
while True:
    user = int(input('주사위 값은 얼마일까요? >>> '))
    if dice == user:
        print('{}! 정답입니다.'.format(dice))
        break
    else:
        print('오답입니다. 다시 시도하세요.')

print()

# time모듈, datetime 모듈

# ex) 모듈과 조건문을 이용한 계절 구하기
import datetime

now = datetime.datetime.now()    # pc로 부터 현재 날짜, 시간 추출
m = now.month   # 추출한 현재 날짜 시간 변수의 월만 따로 저장

if 3 <= m <= 5: # 만약 월이 3, 4, 5월이라면
    print('봄')
elif 6 <= m <= 8:
    print('여름')
elif 9 <= m <= 11:
    print('가을')
else:
    print('겨울')

print()

# time 함수
# ex) 모듈을 이용하여 속으로 10초 세어 맞히는 프로그램
import time

input('엔터를 누르고 10초를 셉니다.')
start = time.time()     # 현재 시간 저장

input('10초 후 다시 엔터를 누르세요.')
end = time.time()

elapse = end - start
print(f'실제 시간 :{elapse}')
print(f'차이 :{abs(elapse-10)}초')  # abs() : 절댓값


print()

# p.g 218
from datetime import*

start = datetime.now()
total = 0
for num in range(1, 10000001):
    total += num
end = datetime.now()

elapse = end - start
elapse = elapse.total_seconds()

print('총 합은 {}입니다.'.format(total))
print('총 {}초가 소요되었습니다.'.format(elapse))

print()
