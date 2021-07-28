# 입력 명령어(input)
'''
[문제]
변수 height에 키(tall)를 묻고 값을 할당하시오.
변수 height를 정수형(int)으로 만들어 소수점 아래를 버리시오.
변수 weight에 상대방의 몸무게를 실수형(float)으로 묻고 값을 할당하시오.
변수 height와 변수 weight를 더한 값을 출력하시오.

[출력결과]

키가 얼마인가요? 165
몸무게는 얼마인가요? 50.0
키 + 몸무게 =  215.0

'''
height = int(input('키가 얼마인가요?'))
weight = float(input('몸무게는 얼마인가요?'))
print('키 + 몸무게 =',height + weight)
print()

'''
[문제] : 값을 입력받아 문장 출력하기

[출력결과]

당신의 나이는 몇 살입니까?   30
당신은 30 년을 살았습니다.

'''

age = int(input('당신의 나이는 몇 살입니까?  '))
print('당신은 %d 년을 살았습니다.' %age)
print()


'''
[문제] : 덧셈 계산기

[출력결과]

덧셈 첫 번째 숫자는?  5
덧셈 두 번째 숫자는?  8
두 숫자의 합은 13 입니다.

'''

num1 = int(input('덧셈 첫 번째 숫자는?  '))
num2 = int(input('덧셈 두 번째 숫자는?  '))
print('두 숫자의 합은 %d 입니다.' %(num1+num2))
print()

'''
[문제] : 나눗셈 계산기

[출력결과]

피제수는?  13
제수는?  5
나눗셈의 몫은 2 나머지는 3 입니다

'''

num1 = int(input('피제수는?  '))
num2 = int(input('제수는?  '))
print('나눗셈의 몫은 %d 나머지는 %d 입니다' %(num1, num2))
print()

'''
[문제] : 성적 계산 프로그램

[출력결과]

이름을 입력하세요 : 파이썬
국어 성적을 입력하세요 : 95
수학 성적을 입력하세요 : 98
사회 성적을 입력하세요 : 84
과학 성적을 입력하세요 : 90
영어 성적을 입력하세요 : 79
파이썬 님의 성적은
총합 446 점, 평균 89.2 점 입니다.

'''
name = input('이름을 입력하세요 : ')
ko = int(input('국어 성적을 입력하세요 : '))
math = int(input('수학 성적을 입력하세요 : '))
social = int(input('사회 성적을 입력하세요 : '))
science = int(input('과학 성적을 입력하세요 : '))
en = int(input('영어 성적을 입력하세요 : '))

total = ko+math+social+science+en
avr = float((ko+math+social+science+en)/5)
print(f'{name} 님의 성적은\n총합 {total} 점, 평균 {avr:.1f} 점 입니다.')
print()

'''
[문제]
피타고라스 정리 : 직각삼각형의 빗변의 제곱은 두 직각 변의 제곱합과 같다.
이 때 두 변의 길이는 실수형으로 입력받도록 해보자.

참고 : 빗변 제곱값 = 첫 번째 직각변의 길이 제곱값 + 두 번째 직각 변의 길이 제곱값
빗변 = 빗변 제곱값 ** 0.5 (제곱을 원래 값으로 하기 위해 1/2(0.5)를 거듭제곱한다. = 제곱근 구하는 것임)

[출력결과]

첫 번째 직각변의 길이(cm) : 15.3  
두 번째 직각변의 길이(cm) : 12.1
빗변의 길이는 19.50640920313116 cm입니다.

'''

num1 = float(input('첫 번째 직각변의 길이(cm) : '))
num2 = float(input('두 번째 직각변의 길이(cm) : '))
slide1 = float(num1**2 + num2**2)
slide2 = float(slide1 ** 0.5)
print(f'빗변의 길이는 {slide2}cm 입니다.')
print()

'''
[문제]
원의 넓이 구하기 : 원의 둘레(2 * 3.14 * 반지름), 원의 넓이(3.14 * 반지름 * 반지름)
이 때 결과값이 소수 둘째자리까지 나오도록 반올림한다. (round사용)

round함수 --> 반올림을 구해주는 함수
                   round(숫자, 자릿수)

[출력결과]

원의 반지름을 입력하세요(cm) : 3
원의 둘레는 18.84 cm이고 원의 넓이는 28.26 cm입니다.

'''

r = int(input('원의 반지름을 입력하세요(cm) : '))
l = 2 * 3.14 * r
s = round(3.14 * r**2, 2)
print(f'원의 둘레는 {l}cm 이고 원의 넓이는 {s}cm 입니다.')
print()

'''
[문제] : 이름을 넣어 새해 인사 문자 보내기

[출력결과]

첫번째 이름을 입력하세요 : 라이언
두번째 이름을 입력하세요 : 어피치
세번째 이름을 입력하세요 : 무지
라이언 님 올 2019년에도 새해 복 많이 받으시고 만수무강 하세요.
어피치 님 올 2019년에도 새해 복 많이 받으시고 만수무강 하세요.
무지 님 올 2019년에도 새해 복 많이 받으시고 만수무강 하세요.

'''
name1 = input("첫 번째 이름을 입력하세요 : ")
name2 = input("두 번째 이름을 입력하세요 : ")
name3 = input("세 번째 이름을 입력하세요 : ")

print(name1, ' 님 올 2019년에도 새해 복 많이 받으시고 만수무강 하세요.')
print(name2, ' 님 올 2019년에도 새해 복 많이 받으시고 만수무강 하세요.')
print(name3, ' 님 올 2019년에도 새해 복 많이 받으시고 만수무강 하세요.')

'''
[문제] : BMI(체질량지수) 계산하기
BMI 공식 = 몸무게 / (키 / 100) ** 2
BMI는 반올림하여 소수 둘째자리까지 나타내기 (round함수 사용)

[출력결과]

이름을 입력하세요 : 파이썬
키(cm)를 입력하세요 : 176
몸무게(kg)를 입력하세요 : 72

파이썬님의 키는  176 cm이고 몸무게는  72 kg 입니다.
BMI 지수는  23.24 입니다.

'''
name = input('이름을 입력하세요 : ')
height = int(input('키(cm)를 입력하세요 : '))
weight = int(input('몸무게(kg)를 입력하세요 : '))

bmi = round(weight/(height/100)**2, 2)

print('{}님의 키는 {}cm이고 몸무게는 {}kg 입니다.\nBMI 지수는 23.24입니다.'.format(name, height, weight, bmi))
