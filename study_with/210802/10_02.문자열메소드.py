# 메소드
'''
    호출 방식 : 객체 뒤에 마침표(.)를 붙이고 호출
'''

# 문자열 메소드

# count() : 특정 문자열의 개수
s = '내가 그린 기린 그림은 목 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다.'
print(s.count('기린'))
print()

s = 'best of best'
print(s.count('best', 5))   # 시작 인덱스 지정
print(s.count('best', -7))
print()

# find(), index() : 특정 문자열 찾기 -> 인덱스 반환
s = 'apple'
print(s.find('p'))
print(s.index('p'))
print(s.find('z'))  # 찾는 문자열이 존재X -> -1 반환
# print(s.index('z'))  # 찾는 문자열이 존재X -> 에러 발생
print()

s = 'best of best'
print(s.find('best', 5))   # 시작 인덱스 지정
print(s.find('best', -7))
print()

print(s.rfind('best')) # rfind() :  오른쪽부터 탐색
print()

# 대소문자 변환 메소드
s = 'BEST of best'
print(s.upper())    # 대문자
print(s.lower())    # 소문자
print(s.capitalize())   # 첫 글자만 대문자
print()


# join() : 합치기
a = '-'.join('python')
print(a)

b = '+'.join(['a', 'b', 'c', 'd', 'e'])
print(b)

c = ''.join(['x','y','z'])
print(c)

d = ''.join({'a':'apple','b':'banana'}) # 딕셔너리의 key 연결하여 반환, value 사용X
print(d)

print()

# split() : 리스트 형식으로 나누기
s = 'Life is too short'
print(s.split())    # 공백을 기준으로 분리
print()

s = '010-1234-5678'
print(s.split('-'))    # 하이폰(-) 기준으로 분리
print()

s = '제임스,25,남,서울'
print(s.split(','))
print()

#replace() : 일부 문자열을 -> 다른 문자열 변환
s = 'Life is too short'
print(s.replace('short', 'long'))
print()

s = '010-1234-5678'
print(s.replace('-', ''))
print()

# strip() : 불필요한 문자열 제거 메소드
s = '   apple'
print(len(s))
a = s.lstrip()   # 왼쪽 끝 제거
print(len(a))
print()

s = 'banana   '
print(len(s))
b = s.rstrip()   # 오른쪽 끝 제거
print(len(b))
print()

s = '   peach      '
print(len(s))
c = s.strip()   # 양쪽 끝 제거
print(len(c))
print()

e = '<head<'
print(e.strip('<'))
print()

# p.g 173
while True :
    p = input('하이폰을 포함하여 전체 주민등록번호를 입력하세요 >>> ')
    if p.find('-') != 6:
        print('하이폰의 위치가 잘못되었습니다.')
        continue
    birthday = p.split('-')[0]
    print('생년월일은 {}입니다.'.format(birthday))
    break
print()
