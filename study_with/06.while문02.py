# p.g 107
my_list = []
n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))
while n != 0 :
    my_list.append(n)
    n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))
print(my_list)

print()

# TIP
my_list = []
n = 1   # 0이 아닌 초기값 실행 -> while문 실
while n != 0 :
    n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))
    my_list.append(n)

# pop() : 리스트의 마지막 요소를 뽑은 후 제거
# pop(리스트 요소 위치) : 리스트 위치의 요소를 뽑은 후 제
my_list.pop()   # my_list의 마지막 요소는 언제나 0이므로 제거
print(my_list)

print()

# 중첩 while문
day = 1
while day <= 5 :
    hour = 1
    while hour <= 3:
        print('{}일차 {}교시 입니다.'.format(day, hour))
        hour += 1
    day += 1

# p.g 110
dan = 2
while dan <= 9:
    n = 1
    while n <= 9:
        print('{} X {} = {}'.format(dan, n, dan*n))
        n += 1
    dan += 1
