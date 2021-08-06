# p.g 221
# 01.
import random
import time

pot = [n for n in range(1, 46)]
jackpot = []

for n in range(1, 7):
    random.shuffle(pot)
    pick = pot.pop()
    print(f'{n}번째 당첨번호는 {pick}입니다.')
    jackpot.append(pick)
    time.sleep(2)

jackpot.sort()
print(f'이번 당첨번호는 {jackpot} 입니다.')

print()

# p.g 222
# 02.
import math

print('UpDown게임을 시작합니다.')
ans = random.randint(1, 100)
start = time.time()
while True:
    n = int(input('어떤 값일까요? >>> '))
    if n == ans:
        print('정답입니다.')
        break
    elif n > ans:
        print('Down')
    else:
        print('UP')
        
end = time.time()

elapse = end - start
print('{}초 만에 성공했습니다.'.format(math.floor(elapse)))

print()
