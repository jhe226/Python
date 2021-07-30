# 참고) 리스트 내포(리스트 컴프리헨션)
#append() 사용
num = []
for n in [1, 2, 3] :
    num.append(n*2)
print('append 사용 : ', num)

print()

# 리스트 내포 사용
num2 = [n*2 for n in [1, 2, 3]]
print('리스트 내포 사용 : ', num2)

print()

# append, if 사용
num3 = []
for n in [1, 2, 3, 4, 5] :
    if n % 2 == 1:  # 홀수만
        num3.append(n*2)
print('append, if 사용 : ', num3)

# 조건을 만족하는 데이터만 출력하는 리스트 내포
num4 = [n*2 for n in [1, 2, 3, 4, 5] if n%2==1]
print('조건 리스트 내포 사용 : ', num4)
