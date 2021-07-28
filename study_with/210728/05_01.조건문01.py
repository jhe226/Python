# 조건문
# if문

a = 99

if a < 100:
    print('100보다 작군요!')

print()

num = int(input('정수를 입력하세요: '))
if num>0:
    print('양수입니다.')
elif num == 0:
    print('0입니다.')
else :
    print('음수입니다.')

print()

# p.g 95
age = int(input('몇 살입니까? >>> '))
if age>=20:
    print('성인')
else :
    print('미성년자')

print()

# ex) 값을 입력받아 짝수, 홀수 구분하기
num1 = int(input('정수를 입력하세요 : '))

if num%2 == 0:
    print("짝수")
else :
    print("홀수")

print()

# ex2)
s = input('아이디를 입력하세요 : ')

if s== id1:
    print('환영합니다!')
else :
    print('아이디를 찾을 수 없습니다.')
    
print()

# ex3) 값을 입력받아 in 연산자를 이용하여 짝수, 홀수 구분하기

num2 = input('정수를 입력하세요 : ')    # 문자열 형식으로 입력받을 것
a = num2[-1]

if a in '02468':        # 만약 맨 끝 글자가 02468 안에 있는 글자라면
    print('짝수')
else :
    print("홀수")

print()
