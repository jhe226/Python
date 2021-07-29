# for
'''
    반복 횟수가 정해져 있을 때 사용

    <형식>
     for 변수 in 리스트명 :
         반복할 코드

     for 변수 in range(횟수) :
         반복할 코드
         
     for 변수 in range(시작값, 끝값 + 1) :
         반복할 코드
'''
# 시퀀스와 for문

# for문과 list

for n in [1, 2, 3] :
    print(n)

print()

for item in ['가위' ,'바위', '보'] :
    print(item)

print()

# for문과 문자열
for ch in 'Hello' :
    print(ch)

print()

# for문과 튜플
four_seasons = ('Spring', 'Summer', 'Autumn', 'Winter')
for season in four_seasons :
    print(season)

print()

# p.g 120
pwd = input('비밀번호를 입력하세요 >>> ')
ch_count = 0
num_count = 0

for ch in pwd :
    if ch.isalpha() :
        ch_count += 1
    elif ch.isnumeric() :
        num_count += 1

if ch_count > 0 and num_count > 0 :
    print('가능한 비밀번호입니다.')
else :
    print('불가능한 비밀번호입니다.')

# ch.isalpha(): ch가 문자인 경우 True 반환
# ch.isnumeric() : ch가 숫자인 경우 True 반환

print()


# for문과 range()
for i in range(10) :    # 10번 반복 (0~9) -> 초기값 X
    print(f'{i}번째 문장입니다.')

print()


for i in range(1, 11) : # 10번 반복 (1~10) -> 초기값 O
    print(f'{i}번째 문장입니다.')

print()


for i in range(10, 0, -1) : # 10부터 1까지 1씩 감소
    print(f'{i}번째 문장입니다.')
    
print()


for i reversed(range(10)) : # 9부터 0까지 출력
    print(f'{i}번째 문장입니다.')

print()


count = int(input('반복할 횟수를 입력하세요 : ')
for i in range(1, count+1) :
    print(f'{i}번째 문장입니다.')

print()

# ex) 1부터 100까지 수 중 3의 배수
for i in range(1, 101) :
    if i % 3 == 0 :
        print(f'{i} : 3의 배수')
    else :
        print(i)

print()


# p.g 125
dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(1, 10) :
            print('{} X {} = {}'.format(dan, n, dan*n))
                      
print()

# 중첩 for문을 이용한 구구단 만들기
for i in range(2, 10) :
    print('======{}단======')
    for j in range (1, 10) :
        print('{} X {} = {}'.format(i, j, i*j))
                      
print()
