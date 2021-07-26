# format() 메서드
'''
    <형식>
    '문자열 {}'.format(변수 또는 상수)
'''

# p.g 60

zipcode = '06236'
print('우편번호 : {}'.format(zipcode))

address = '''서울 특별시 강남구
테헤란로 146'''
print('주소 : {addr}'.format(addr=address))

tel1, tel2, tel3 = '02', '538', '0021'
print('연락처 : {}-{}-{}'.format(tel1, tel2, tel3))
print()


print('{0:<10}'.format('Hi'))   # 전체 10칸, 왼쪽 정렬
print('{0:>10}'.format('Hi'))   # 전체 10칸, 오른쪽 정렬
print('{0:^10}'.format('Hi'))   # 전체 10칸, 가운데 정렬
print()

print('{:=^30}'.format('Python'))   # 전체 30칸, 공백 : =로 표현 , 가운데 정렬
print('{:!<30}'.format('Python'))   # 전체 30칸, 공백 : !로 표현 , 왼쪽 정렬
print('{:*>30}'.format('Python'))   # 전체 30칸, 공백 : *로 표현 , 오른쪽 정렬
print()

n = 3.141592
print('{:.3f}'.format(n))   # 소수 셋째자리까지 나타냄
print()


print('{{Python}}'.format())    # 중괄호 표현
print()

a = '파이썬 열공하여 첫 연봉 {}만원 만들기'.format(5000)
b = '{} {}       {}'.format(100, 200, 300)
c = '{} {} {}'.format(1, '파이썬', True)

print(a)
print(b)
print(c)
