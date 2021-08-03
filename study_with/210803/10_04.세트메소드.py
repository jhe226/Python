# 세트 메소드
s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}

print('세트1 :', s1)
print('세트2 :', s2)
print()

# 교집합
print(s1 & s2)
print(s1.intersection(s2))
print()

# 합집합
print(s1|s2)
print(s1.union(s2))
print()

# 차집합
print(s1 - s2)
print(s1.difference(s2))
print()
