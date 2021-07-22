# 자료형

'''
    프로그래밍할 때 쓰이는 숫자, 문자열 등 자료형태로 사용하는 모든 것

    다른 언어의 경우, 변수 설정시 타입을 직접 설정해야하는 경우가 많음.
    파이썬의 경우 값을 할당하면 그 때 타입이 자동으로 결정됨.

    type 함수로 자료형을 볼 수 있다.
'''

# 정수
print(int(1.9))
print(int(True))    # True : 1
print(int(False))   # False : 0
print(int('100'))
print()

n = 95
print(bin(n))   # 2진수 (0, 1)
print(oct(n))   # 8진수 (0 ~ 7)
print(hex(n))   # 16진수 (0 ~ 9, A ~ F)
print()

# 실수
print(float(1))
print(float(True))
print(float(False))
print(float('3.14'))
print(float('100'))
print()

# 논리
print(bool(0))
print(bool(1))
print(bool(2))  # 0을 제외한 나머지 숫자 = True
print(bool(''))
print(bool([]))
print()

# 문자열
print('Hello, World!')
print("Hello, World!")
print('''Life is too short,
            you need python.''')
print("It's me") #  어퍼스트로피(') 사용 시 편리함
print('"This is so easy to learn", he said.')   # 인용문 넣을 때
print()

print(str(100))
print(str(True))
print(str(False))
print(str(3.14))
print()

# 문자열 인덱싱 (Indexing)
'''
    [0] : 문자열의 처음
    [-1] : 문자열의 마지막
'''

print('안녕하세요'[0])
print('안녕하세요'[1])
print('안녕하세요'[2])
print('안녕하세요'[3])
print('안녕하세요'[4])
print()

print('안녕하세요'[-1])
print('안녕하세요'[-2])
print('안녕하세요'[-3])
print('안녕하세요'[-4])
print('안녕하세요'[-5])
print()

a = 'My python'
print(a[0])
print(a[2])
print(a[3])
print(a[-1])
print()

# 문자열 슬라이싱 (Slicing)
'''
    문자열의 구간을 표시
    a[시작번호:끝번호+1]

    [:] --> 처음부터 끝까
'''

print('안녕하세요'[1:3])
print('안녕하세요'[2:4])
print()

a = 'python'
print(a[0:2])
print(a[:])
print(a[-2:-1])
print(a[:3])
print(a[2:])
print()
