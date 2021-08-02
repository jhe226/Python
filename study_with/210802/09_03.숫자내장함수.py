# 숫자 내장 함수
# abs() : 절대값
print(abs(10))
print(abs(-10))
print()

# divmod() : (몫,나머지) 출력. 튜플 형식
divmod(10, 3)
d, v = divmod(5, 2)
print(d)
print(v)
print()

# max() : 가장 큰 값 반환
print(max(1, 10))

li = [5, 4, 3, 2, 1]
print(max(li))

print()

# min() :가장 작은 값 반환
print(min(1, 10))

li = [5, 4, 3, 2, 1]
print(min(li))

print()

# pow() : 거듭제곱 (** 연산자)
print(pow(10, 2))
print()

# round() : 반올림
print(round(1.5))
print(round(1.55, 1))
print(round(2.6798, 3))
print()

# sum() : 합계
li = [5, 4, 3, 2, 1]
print(sum(li))
print()

# p.g 153
money = 10000
price = 3000
result = divmod(money,price)
print('빵을 {}개 사고 {}원이 남았습니다.'.format(result[0], result[1]))

print()

'''
    money = 10000
    price = 3000
    bread, change = divmod(money,price)
    print('빵을 {}개 사고 {}원이 남았습니다.'.format(bread, change))

'''

