# 여러 개의 변수

a, b, c = 1, 2, 3 # 변수 값을 대입할 때 한 번에 순서대로 대입, 짝이 맞아야 함
print(a)
print(b)
print(c)
print()

a = b = c = 4   # 여러 개의 변수에 한 번에 같은 값 대입 가능
print(a)
print(b)
print(c)
print()

# 변수의 교환

a = 1
b = 2

print('변수 a :', a)
print('변수 b :', b)
print()

a, b = b, a # 변수끼리 맞교환 가능 (tmp 필요 x)
print('변수 a :', a)
print('변수 b :', b)
print()
