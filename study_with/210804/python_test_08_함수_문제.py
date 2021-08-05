# 함수

'''
[문제] 사칙 연산 함수 만들기

숫자 두개로 덧셈, 뺄셈, 곱셈, 나눗셈의 결과가 나오도록 하시오.
(단, 각각의 연산은 함수를 이용해서 만들것)

예) 덧셈코드

def add(x, y):
    덧셈 계산 코드 넣기

나머지 계산코드도 이런식으로 만들기


[출력결과] (매개변수 x를 10으로, 매개변수 y를 20으로 한 결과)
30
-10
200
0.5

'''

def add(x, y):
    print(x+y)

def sub(x, y):
    print(x-y)

def mul(x, y):
    print(x*y)

def div(x, y):
    print(x/y)

add(10, 20)
sub(10, 20)
mul(10, 20)
div(10, 20)

print()
print()

'''
[문제]

회원등급에 따른 할인율 계산하여 출력하기
매개변수가 2개인(회원등급, 가격)
하나의 함수로 만들어보기

'S' --> 할인율 5%
'G' --> 할인율 10%
'V' --> 할인율 15%


[출력결과]
회원 등급을 입력하세요 : V
가격을 입력하세요 : 20000
3000 원입니다.

'''
rank = input('회원 등급을 입력하세요 : ')
price = int(input('가격을 입력하세요 : '))
    
def memberhship(rank, price):
    money = 0
    if rank == 'S':
        money = int(price * 0.05)
        print(money, '원 입니다.')
    elif rank == 'G':
        money = int(price * 0.10)
        print(money, '원 입니다.')
    elif rank == 'V':
        money = int(price * 0.15)
        print(money, '원 입니다.')
    else :
        print('할인 대상이 아닙니다.')
        
memberhship(rank, price)

print()
print()

'''
[문제]

아래의 출력결과와 같이 이름을 받아서 생일 축하 노래를 출력하는 함수 happyBirthday()를 만들고 호출하여 실행해보시오.

[출력결과]
Happy Birthday to you!
Happy Birthday to you!
Happy Birthday, dear 홍길동
Happy Birthday to you!

Happy Birthday to you!
Happy Birthday to you!
Happy Birthday, dear 라이언
Happy Birthday to you!

'''
def happyBirthday(name) :
    print('''Happy Birthday to you!
Happy Birthday to you!
Happy Birthday, dear {}
Happy Birthday to you!'''.format(name))
    print()

happyBirthday('홍길동')
happyBirthday('라이언')

print()

'''
[문제]

원주율을 나타내는 변수 PI = 3.14를 만들고, 반지름을 입력 받은 후
원의 면적을 계산하는 함수, 원의 둘레를 계산하는 함수를 호출하여 실행시켜 보시오.

[출력결과]
반지름을 입력하세요 : 5
반지름 5의 원의 넓이는 78.5이고,
원의 둘레는 31.400000000000002입니다.

'''
PI = 3.14
r = int(input('반지름을 입력하세요 : '))
def area(R):
    a = PI * R * R
    return a

def length(R) :
    l = 2*PI*R
    return l

A = area(r)
L = length(r)

print('반지름 {}의 원의 넓이는 {}이고,'.format(r, A))
print('원의 둘레는 {}입니다.'.format(L))

print()
print()

