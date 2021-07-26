# 문자열 포매팅 (formatting)
'''
[문제]
변수 number에 숫자 5를 담고
아래의 출력결과와 같이 출력되도록 하시오.
포매팅 형식은 기본 포매팅, format 함수 포매팅, f 문자열 포매팅
3가지 방식으로 표현하시오.


[출력결과]
I eat 5 apples.  --> 기본 포매팅 형식
I eat 5 apples.  --> format 함수 포매팅 형식
I eat 5 apples.  --> f 문자열 포매팅 형식

'''

n = 5

print('I eat %d apples.' %n)
print('I eat {} apples.'.format(n))
print(f'I eat {n} apples.')

print()

'''
[문제]
변수 num1에 숫자 3을 담고, 변수 num2에 숫자 5를 담은 후
아래의 출력결과와 같이 출력하시오.
이번 포매팅 형식은 format 함수 포매팅, f 문자열 포매팅
2가지 방식으로 표현하시오.


[출력결과]
I eat 3 apples. You eat 5 apples.
I eat 3 apples. You eat 5 apples.

'''

num1 = 3
num2 = 5

print('I eat {} apples. You eat {} apples.'.format(num1, num2))
print(f'I eat {num1} apples. You eat {num2} apples.')

print()

'''
[문제] 위의 문제 응용
변수 num1에 input 함수를 이용해서 숫자를 입력받도록 한다.
변수 num2에 input 함수를 이용해서 숫자를 입력받도록 한다.
아래의 출력결과와 같이 출력하시오.
이번에도 포매팅 형식은 format 함수 포매팅, f 문자열 포매팅
2가지 방식으로 표현하시오.


[출력결과]
첫번째 숫자를 입력하세요 : 10  --> 여기서 10은 실행 후 우리가 입력
두번째 숫자를 입력하세요 : 20  --> 여기서 20은 실행 후 우리가 입력
I eat 10 apples. You eat 20 apples.
I eat 10 apples. You eat 20 apples.

'''

num1 = int(input('첫 번째 숫자를 입력하세요 : '))
num2 = int(input('두 번째 숫자를 입력하세요 : '))

print('I eat {} apples. You eat {} apples.'.format(num1, num2))
print(f'I eat {num1} apples. You eat {num2} apples.')











