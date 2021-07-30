# 내장 함수
# 문자열 내장 함수
# chr() : 유니코드를 문자로 변환
print(chr(48))
print(chr(49))
print(chr(65))
print(chr(66))
print(chr(97))
print(chr(98))

print()

# ord() : 문자를 유니코드로 변환
print(ord('A'))
print(ord('한'))

print()
      
# eval() : 문자열로 된 값 계산
print(eval('100 + 200'))
a = 10
print(eval('a * 5'))
print(eval('min(1,2,3)'))
print()

# format() : 형식을 갖춘 문자열
print(format(10000, ','))    # 천단위 구분 기호 넣기
print(format(10000, '_'))
print()

# p.g 149
expr = input('계산식을 입력하세요 >>> ')
result = eval(expr)
print(expr + '=' + str(result))
print()
