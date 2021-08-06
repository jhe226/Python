# 파일 입출력
# 파일 생성하고 문자열 쓰기
'''
    <형식> (기본방법)
    파일 객체명 = open('파일 이름', 'w')
    파일 객체명.write('문자열')
    파일 객체명.write(str(숫자))   # write 함수는 문자 형식만 가능
    파일 객체명.close()

    <형식> (리스트 사용)
    리스트명 = [값1, 값2, ...]
    파일 객체명 = open('파일 이름', 'w')
    파일 객체명 = writelines(리스트명)
    파일 객체명.close()
    
'''

file = open('hello.txt', 'w')   # 파일 열기(쓰기 모드 -> 기존 내용 지우고 덮어쓰기)
file.write('Hello, World!')
file.close()

print()

# for문을 이용하여 파일에 문자열 쓰기
file = open('hello.txt', 'w')
# 'C:/a/hello.txt'  --> c드라이브 안 a라는 폴더에 hello.txt 파일 생성 (절대 주소)

# 상대 경로 : 현재 폴더 기준
# 절대 경로 : 직접 기입 (C:\...\...)    -> 파이썬은 슬래시(/)와 역슬래시(\)모두 사용 가능 (원칙은 역슬래시)

for i in range(1, 11):
    data = f'{i}번째 줄입니다.\n'
    file.write(data)    # write 함수는 엔터 기능이 없다.

file.close()    # 파일 닫기
print()

# for문을 이용하여 파일에 새로운 내용 추가하기
file = open('hello.txt', 'a')   # 파일 열기(추가 모드 -> 기존 내용 남아있음)

for i in range(11, 21):
    data = f'{i}번째 줄입니다.\n'
    file.write(data)

file.close()
print()

# 파일에서 문자열 읽기
'''
    <형식>
    파일 객체명 = open('파일 이름', 'r')
    변수명 = 파일 객체명.read()
    파일 객체명.close()
    
    print(변수명)
'''

f = open('hello.txt', 'r')
a = f.read()    # 읽은 내용을 a변수에 담음
f.close()

print(a)    # a 변수의 내용을 화면에 출력
print()

# 파일에서 여러 줄을 리스트로 각각 읽기
'''
    <형식>
    파일 객체명 = open('파일 이름', 'r')
    리스트명 = 파일 객체명.readlines()
    파일 객체명.close()
    
    print(리스트명)
'''
f = open('hello.txt', 'r')
lines = f.readlines()    # 파일에서 읽은 내용을 리스트 형태로 저장
f.close()

print(lines)    # 리스트 형식인지 확인
print()

for i in lines:     # 여러 줄을 한 줄씩 차례로 출력
    print(i, end = '')
print()

# with문과 함께 파일 입출력하기
'''
    파일을 열면 항상 close 해주어야 하는 불편함을 덜어주는 기능

    <형식>
    with open('파일 이름', '파일 열기 모드') as 파일 객체명:
        수행할 코드
'''
list_a = ['Hello\n', 'World!\n', 'Python\n', 'Learning\n']

with open('file.txt', 'w') as f:    # 쓰기 모드
    f.writelines(list_a)    # 리스트를 파일에 쓸 때
    f.write('LoL\n')
    f.write('파이썬을 공부해봅시다.\n')

with open('file.txt','r') as f:     #읽기 모드
    b = f.read()    # 파일의 내용을 모두 읽어 b 변수에 담았다.

print(b)
print()

# p.g 232
import time

file = open(time.strftime('%Y-%m-%d')+'.txt', 'a')

while True:
    schedule = input('오늘의 스케줄을 입력하세요 >>> ')
    if not schedule:
        break
    file.write(schedule + '\n')
    
file.close()
print()

# p.g 237
file = open('엄마돼지아기돼지.txt', 'rt')

line_list = file.readlines()

cnt = 0
for line in line_list:
    for char in line:
        if char == '꿀':
            cnt += 1
print('꿀은 전체 {}번 나타납니다.'.format(cnt))
print()
