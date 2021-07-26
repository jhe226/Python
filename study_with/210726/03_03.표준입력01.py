# 표준입력 input()

# p.g 63

name = input('이름을 입력하세요 >>> ')
age = input('나이를 입력하세요 >>> ')

print('입력된 이름은 {}입니다.'.format(name))
print('입력된 나이는 {}살입니다.'.format(age))
print()


s = input('입력 : ')
print('변수 s의 값 : ', s)
print('변수 s의 자료형(타입) : ', type(s))
print()

a = int(input('입력 : ')) # 정수형으로 형 변환
print('변수 a의 값 : ', a)
print('변수 a의 자료형(타입) : ', type(a))
print('a + 100 = ', a + 100)
print()

s1 = input('입력 s1 : ')
s2 = input('입력 s2 : ')
print('s1 + s2 = ', s1 + s2)    # s1, s2를 문자로 받아들임  -> 두 문자를 이어붙임
print()

i1 = int(input('입력 s1 : '))
i2 = int(input('입력 s2 : '))
print('s1 + s2 = ', i1 + i2)  # s1, s2를 정수로 형 변환 -> 정수로 받아들임 -> 정수의 연산 결과 출력
print()

