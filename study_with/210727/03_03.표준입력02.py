# 실수형으로 입력받기
num1 = float(input('실수로 된 숫자 : '))
num2 = float(input('실수로 된 두 번째 숫자 : '))
print()

print('덧셈 결과 : ', num1+num2)
print('뺄셈 결과 : ', num1-num2)
print('곱셈 결과 : ', num1*num2)
print('나눗셈 결과 : ', num1/num2)
print()

# p.g 65
price = 50000
n = int(input('할부 개월 입력 : '))
print('매달 내는 돈은 {}원입니다.'.format(price/n))

