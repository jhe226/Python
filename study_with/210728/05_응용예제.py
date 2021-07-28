# p.g 99
# 01.
score = int(input('점수를 입력하세요 >>> '))
if score >= 90 :
    print(f'점수는 {score}점이고, 학점은 A학점 입니다.')
elif score >= 80 :
    print(f'점수는 {score}점이고, 학점은 B학점 입니다.')
elif score >= 70 :
    print(f'점수는 {score}점이고, 학점은 C학점 입니다.')
elif score >= 60 :
    print(f'점수는 {score}점이고, 학점은 D학점 입니다.')
else :
    print(f'점수는 {score}점이고, 학점은 F학점 입니다.')

print()

# 02.
num = int(input('정수를 입력하세요 >>> '))
if num%3 == 0:
    print(f'{num}는 3의 배수입니다.')
else :
    print(f'{num}는 3의 배수가 아닙니다.')
print()

# 03.
n1 = int(input('정수1 입력 >>> '))
n2 = int(input('정수2 입력 >>> '))
n3 = int(input('정수3 입력 >>> '))

if n1 < n2 :
    if n2 < n3 :
        print(f'가장 큰 수는 {n3}입니다.')
    elif n3 < n1 :
        print(f'가장 큰 수는 {n2}입니다.')
elif n2 < n1 :
    if n1 < n3 :
        print(f'가장 큰 수는 {n3}입니다.')
    elif n3 < n1 :
        print(f'가장 큰 수는 {n1}입니다.')
    else :
        print(f'가장 큰 수는 {n1}입니다.')
print()

# 04.
number = input('차량번호를 입력하세요 >>> ')
a = number[-1]
if a in '02468':
    print(f'{number}는 오늘 운행가능입니다.')
else:
    print(f'{number}는 오늘 운행불가입니다.')
print()
