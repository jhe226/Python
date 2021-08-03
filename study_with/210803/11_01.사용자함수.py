# 사용자 함수
# 함수 용어 정리
'''
    입력 : 매개변수, 인수, 인자, 파라미터
    출력값 : 반환값, 결과값, return값
'''

# 매개변수(입력값)X, 반환값(출력값)X 가장 간단한 함수
'''
    <형식>
    def 함수이름():  # 함수 정의
        수행 코드

    함수 이름() # 함수 호출
    
'''

def hello():    # 함수 정의
    print('Hello, Python!')
hello()     # 함수 호출
print()

# 매개변수O, 반환X 함수
'''
    <형식>
    def 함수이름(매개변수1, 매개변수2):  # 함수 정의
        수행 코드
    함수이름(인수1, 인수2)   # 함수 호출
    
'''

def introduce(name, age):
    print('내 이름은 {}이고, 나이는{}입니다.'.format(name, age))
introduce('james', 25)
print()

def add(a,b) :
    print(a+b)

add(1, 2)

x = 6
y = 3
add(x, y)

print()

# 가변 매개변수 : 모든 인수를 튜플로.
'''
    <형식>
    def 함수이름(*매개변수1):  # 함수 정의
        수행 코드
    함수이름(인수1, 인수2,...)   # 함수 호출
    
'''

# 디폴트 매개변수 : 매개변수에 초기값
def greet(message = '안녕하세요'):
    print(message)

greet('반갑습니다.') # 디폴트 매개변수 값은 직접 입력을 통해 바꿀 수 있음
greet()
print()

def info(name, age, address = '비공개'):
    print('이름 :', name)
    print('나이 :', age)
    print('주소 :', address)
    print()

info('네오', 25)  # 주소값을 넣지 않았음에도 주소값을 가짐
print()

# p.g 191
def adder(*args):
    print('{}의 합은 {}입니다.'.format(args,sum(args)))
adder(1, 2)
adder(1, 2, 3)
adder(1, 2, 3, 4)
print()

# 매개변수, 반환 1개인 함수
'''
    <형식>
    def 함수이름(매개변수1, 매개변수2):  # 함수 정의
        수행 코드
        return 반환값
    결과변수명 = 함수이름(인수1, 인수2)   # 함수 호출
'''
def add(a,b) :
    return a+b
print(add(10, 20))
print()

# 매개변수, 반환 2개 이상인 함수
'''
    <형식>
    def 함수이름(매개변수1, 매개변수2):  # 함수 정의
        수행 코드
        return 반환값1, 반환값2
    결과변수1, 결과변수2 = 함수이름(인수1, 인수2)   # 함수 호출
'''
def add_sub(a,b) :
    return a+b, a-b
print(add_sub(10, 20))  # 튜플형식으로 반환
print()

x, y = add_sub(10, 20)
print(x)
print(y)
print()

# p.g 195
def coffee_machine(money, pick):
    print('{}원에 {}를 선택하셨습니다.'.format(money, pick))
    menu = {'아메리카노' : 1000, '카페라떼' : 1500, '카푸치노':2000}
    if pick not in menu:
        print('{}는 판매하지 않습니다.'.format(pick))
        return money,'없는 메뉴'
    elif menu[pick]>money:
        print('{}는 {}원입니다.'.format(pick, menu[pick]))
        return money, '금액 부족'
    else:
        return money-menu[pick],pick

order = input('커피를 선택하세요.(아메리카노, 카페라떼, 카푸치노) >>> ')
pay = int(input('얼마를 내시나요? >>> '))

change, coffee = coffee_machine(pay, order)
print('잔돈 {}원, 커피 {}'.format(change, coffee))
