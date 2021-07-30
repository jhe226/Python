# p.g 111
# 01.
n = int(input('정수를 입력하세요 >>> '))
if n <= 0 :
    print('잘못된 입력입니다.')
else :
    while n != 0 :
        print('{}번째 Hello'.format(n))
        n -= 1
print()

# 02.
n = 1
while n <= 100:
    if n % 7 == 0:
        print(n)
    n += 1

print()

# p.g 112
# 03.
money = int(input('자판기에 얼마를 넣을까요? >>> '))
n = 1

while n <= money // 300 :
    change = money - n * 300
    print('커피 {}잔, 잔돈 {}원'.format(n, change))
    n += 1

print()

# 04.
list = []
cnt = 0
while True:
    num = int(input('0 ~ 9 사이 정수를 입력하세요 >>> '))
    if num not in list :
        list.append(num)
        cnt += 1
    if cnt == 5 :
        break
print('모두 입력되었습니다.\n입력된 값은 {}입니다.'.format(set(list)))

print()

# 05.
'''
cnt = 0
for i in range(1, 101) :
    print('{}'.format(i), end='\t')
    cnt += 1
    if cnt % 10 == 0 :
        print()
'''
cnt = 0
n = 1
while n < 101 :
    print(n, end='\t')
    n += 1
    cnt += 1
    if cnt % 10 == 0 :
        print()
print()

# 06.
n = 1
cnt = 0
while n <= 9:
    dan = 2
    while dan <= 9 :
        if dan*n >= 10 :
            print(f'{dan} x {n} = {dan*n}', end = '   ')
            dan += 1
            cnt += 1
            if cnt % 8 == 0 :
                print()
        elif dan*n < 10 :
            print(f'{dan} x {n} = {dan*n}', end = '')
            dan += 1
            cnt += 1
            if cnt % 8 == 0 :
                print()
    n += 1

