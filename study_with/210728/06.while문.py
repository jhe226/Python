# 반복문
# while문
'''
    <형식 : 반복 횟수가 정해진 경우>
    변수 = 시작값
    while 변수값 < 끝값 :
        반복할 부분
        변수 = 변수 + 증감값

    <형식 : 조건문으로 판단하는 경우>
    변수 = 시작값
    while 조건문 :
        반복할 부분
        
'''

# ex) 100번 출력

i = 0 # 시작값(초기식)
while i < 100 :
    print('Hello, World!')
    i = i + 1
print()

# ex) 무한 반복
'''
while True :
    print('ㅋ', end='') # ctrl+c 누르면 종료
print()
'''

# p.g 105
n = 10
while n>= 1:
    print(n)
    n -= 1
print()

# ex) while문을 이용하여 숫자로 대미지를 입힌 후 체력이 0이 되면 종료하기
hp = 100
while hp > 0 :  # hp <= 0 이면 반복문 종료
    print(f'주인공의 체력은 {hp}입니다.')
    damage = int(input('얼마의 대미지를 입히시겠습니까?'))
    hp -= damage    # hp = hp -damage와 같다.

print(f'주인공의 체력이 0이 되어 종료합니다.') # 반복문 종료 후 실
print()
