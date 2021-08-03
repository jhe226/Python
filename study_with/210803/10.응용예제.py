# p.g 180
# 01.
num = input('전화번호를 입력하세요 >>> ')
phone = num.split('-')[1]
print(phone)
print()

# 02.
num = input('사업자등록번호를 입력하세요(예: 123-45-67890) >>> ')
n1 = num.split('-')[0]
n2 = num.split('-')[1]
n3 = num.split('-')[2]

condition1 = len(num) == 12
condition2 = (num.find('-') == 3)
condition3 = (num.find('-', 4) == 6)
condition4 = (num.replace('-','').isdecimal)

if condition1 and condition2 and condition3 and condition4:
    print('올바른 형식입니다.')
else:
    print('올바른 형식이 아닙니다.')
print()

# p.g 181
# 03.
student = '"김철수", 85'
name = student.split(',')[0].strip('"')
score = student.split(',')[1]
print('이름은 {}이고, 점수는 {}입니다.'.format(name, score))
print()
