# p.g 141
# 01.

money = 10000
print('현재 10000원이 있습니다.')
while True:
    if money == 0:
        break
    spend = int(input('사용할 금액 입력 : >>> '.format(money)))
    if spend <= 0:
        print('0 이하의 금액은 사용할 수 없습니다.\n현재 {}원이 있습니다.'.format(money))
    elif spend > money:
        print('{}원이 부족합니다.\n현재 {}원이 있습니다.'.format(spend-money, money))
    else:
        money -= spend
        print('현재 {}원이 있습니다.'.format(money))

print()

# 02.
while True:
    score = int(input('이번 영화의 평점을 입력하세요 >>> '))
    if score < 1 or score > 5:
        print('평점은 1~5 사이만 입력할 수 있습니다.')
    else:
        print('평점 : {}'.format(score * '★'))
        break

print()

# p.g 142
# 03.
ans = 'qwerty'
cnt = 0
while True:
    if cnt == 5:
        print('비밀번호 입력횟수를 초과했습니다.')
        break
    pwd = input('비밀번호를 입력하세요 >>> ')
    if pwd == ans:
        print('비밀번호를 맞혔습니다.')
        break
    cnt += 1

print()

# p.g 143
# 04.
for dan in range(2, 10):
    if dan % 2 == 0:
        print()
        continue
    for n in range(1, 10):
        if n > dan:
            break
        print('{} x {} = {}'.format(dan, n, dan*n))