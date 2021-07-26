# f-strings (f-문자열 포매팅)
'''
    <형식>
    f'문자열 {변수명} 문자열'    // 반드시 해당 변수명을 써주어야 함
'''

name = '라이언'
age = 20

print(f'나의 이름은 {name}입니다. 나이는 {age}살입니다.')
print('나는 내년이면 {age+1}살이 됩니다.'.format(age))
print()

print(f'{"Hi":=^30}')   # 전체 30칸, 공백 : =, 가운데 정렬
print(f'{"Hi":!<30}')   # 전체 30칸, 공백 : =, 왼쪽 정렬
print()

n = 3.141592

print(f'{n:.3f}')   # 소수 셋째자리까지 반올림
print()

# 포매팅 비교하기

n = 3

print('I eat',n,'apples.')
print('I eat %d apples.' %n)    # % 연산자 포매팅 (기본 포매팅)
print('I eat {} apples.'.format(n)) # format() 포매팅
print(f'I eat {n} apples.') # f-strings 포매팅
print()
