# 기본 연산자
# p.g 73

a = 7
b = 2
print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} ** {} = {}'.format(a,b,a**b))
print('{} / {} = {}'.format(a,b,a/b))
print('{} // {} = {}'.format(a,b,a//b))
print('{} % {} = {}'.format(a,b,a%b))

print()


# 대입 연산자
# p.g 75

a,b = 10, 20
print('a = %d, b = %d' %(a, b))
a, b = b, a
print('a = %d, b = %d' %(a, b))

print()

# 복합 대입 연산자
# ex) a가 10에서 시작해서 코드가 진행될수록 값이 변하도록 해보기

a = 10
print('a의 값 :',a)
a += 5
print('a의 값 :',a)
a -= 5
print('a의 값 :',a)
a *= 5
print('a의 값 :',a)
a **= 5
print('a의 값 :',a)
a /= 5
print('a의 값 :',a)
a //= 5
print('a의 값 :',a)
a %= 5
print('a의 값 :',a)

print()

# p.g 76

piggy_bank = 0

money = 10000
piggy_bank += money
print('저금통에 용돈 {}원을 넣었습니다.'.format(money))
print('지금 저금통에는 {}원이 있습니다.'.format(piggy_bank))

snack = 2000
piggy_bank -= snack
print('저금통에 스낵 구입비 {}원을 뺐습니다.'.format(snack))
print('지금 저금통에는 {}원이 있습니다.'.format(piggy_bank))
print()

# 관계 연산자 : 자동으로 T/F 출력(bool)
# p.g 78

a = 15
print('{}>10 : {}'.format(a, a>10))
print('{}<10 : {}'.format(a, a<10))
print('{}>=10 : {}'.format(a, a>=10))
print('{}<=10 : {}'.format(a, a<=10))
print('{}==10 : {}'.format(a, a==10))
print('{}!=10 : {}'.format(a, a!=10))
print()

# 논리 연산자
# p.g 78

a = 10
b = 0
print('{}>0 and {}>0 : {}'.format(a, b, a>0 and b>0))
print('{}>0 or {}>0 : {}'.format(a, b, a>0 or b>0))
print('not {} : {}'.format(a, not a))
print('not {} : {}'.format(b, not b))
print()

# 비트 연산자 : 2진수로 연산
# p.g 82

a = 10                              #   a = 0000 1010 -> 10
b = 70                              #   b = 0100 0110 -> 70
print('a & b : {}'.format(a&b))     # a&b = 0000 0010 -> 2   
print('a | b : {}'.format(a|b))     # a|b = 0100 1110 -> 78
print('a ^ b : {}'.format(a^b))     # a^b = 0100 1100 -> 76
print('~a : {}'.format(~a))         # ~a  = 1111 0101 -> -11    : 0이면 1, 1이면 0
print('a << 1 : {}'.format(a<<1))   # a << n = 0001 0100 -> 20  : 왼쪽으로 n 이동, 2^n만큼 곱셈
print('a >> 1 : {}'.format(a>>1))   # a >> n = 0000 0101 -> 5   : 오른쪽으로 n 이동, 2^n만큼 나눗셈
print()

# 시퀀스 연산자
# p.g 83

tree = '#'
space = ' '
print(space*4+tree*1)
print(space*3+tree*3)
print(space*2+tree*5)
print(space*1+tree*7)
print(space*0+tree*9)
print()

# 기타 연산자
# 1) 멤버쉽 연산자 (in 연산자)
print('안녕'in'안녕하세요')    # 포함되어있음 -> True 출력
print('잘가'in'안녕하세요')    # 포함되어있지X -> False 출력

print('안녕'not in'안녕하세요')    # 포함되어있음 -> False 출력
print('잘가'not in'안녕하세요')    # 포함되어있지X -> True 출력

# 2) 삼항연산자 : 참if(조건식)else(거짓)
# p.g 84

a = 10
b = 20
result = (a-b)if(a>=b)else(b-a)
print('{}와 {}의 차이는 {}입니다.'.format(a,b,result))
print()
