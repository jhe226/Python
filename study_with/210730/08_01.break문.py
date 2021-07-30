# break문

# ex) 0부터 99까지 출력
i = 0
while True :    # 무한 반복
    print(i, end=' ')
    i = i + 1       # i += 1
    if i == 100 :       # i = 100 이면 반복문 종료
        break
print()

# p.g 136
while True :
    city = input('대한민국의 수도는 어디인가요? >>> ')
    if city == '서울' or city == 'seoul' or city == 'SEOUL' :
        print('정답입니다!')
        break
    else :
        print('오답입니다. 다시 시도하세요.')

print()

# p.g 137
hobbies = []
while True :
    hobby = input('취미를 입력하세요(종료는 그냥 엔터) >> ')
    if hobby == '':     # 'if not hobby : ' 와 같다
        print('입력된 취미가 모두 저장되었습니다.')
        break
    else :
        hobbies.append(hobby)
print(hobbies)

print()
