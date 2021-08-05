# 모듈과 import

# 모듈을 불러와서 사용하기
'''
    import 모듈이름 as 별칭 -->  as 별칭은 생략 가능
    또는
    from 모듈이름 import 모듈함수
    --> 모듈 이름 생략, 함수만 사용하고 싶을 때
    from 모듈 이름 import*
    --> 모듈 안의 모든 함수를 쓰고자 할 때
        모두의 의미를 가진 * 사용
'''

# ex) import 방식
import m    # m이라는 모듈을 가져온다.

print(m.add(1, 2))  # m 모듈 안 add 함수 호출
print(m.sub(2, 1))  # m 모듈 안 sub 함수 호출
print()


# ex) from 방식
from m import add, sub

print(add(1, 2))
print(sub(2, 1))
print()

# ex) from 방식(2)
from m import *

x = int(input('x를 입력하세요 : '))
y = int(input('y 입력하세요 : '))

n1 = add(x, y)
n2 = mul(x, y)

print(n1)
print(n2)
print()

# 패키지(폴더)를 만들어서 관리하는 방법
'''
    <형식>
    import 패키지명.모듈이름 as 별칭
    또는
    from 패키지명.모듈이름 import 모듈함수
'''

# ex)
'''from pkg.m import add, sub # pkg 폴더 안 m 모듈의 add, sub 함수 불러오기

print(add(1, 2))
print(sub(2, 1))
print()
'''
# __name__
'''
    원래 파일에서 실행하면 __name__에 '__main__'이 할당
    모듈로 참조하고 있는 다른 파일에서 실행하면
    __name__에 해당 모듈명이 할당됨
'''

# p.g 208 ~ 209
from my_secure import*

print(secure_name('김철수'))
print(secure_no('951012-1234567'))
print(secure_phone('010-1234-5678'))
print()


