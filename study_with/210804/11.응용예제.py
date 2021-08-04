# p.g 199
# 01.
def vending_machine(money):
    count = money//700
    for i in range(count + 1):
        change = money - 700*i
        print('음료수 = {}개, 잔돈 = {}원'.format(i, change))

vending_machine(3000)

print()
print()

# p.g 200
# 02.
def get_average(marks):
    total = 0
    for sub in marks:
        total += marks[sub]
    avg = total / len(marks)
    return avg

marks = {'국어':90, '영어':80, '수학':85}
average = get_average(marks)
print('평균은 {}점입니다.'.format(average))

print()
print()

# p.g 201
# 03.
total = 0
def gift(dic, who, money):
    global total
    total += money
    dic[who] = money

wedding = {}
gift(wedding, '영희', 5)
gift(wedding, '철수', 3)
gift(wedding, '이모', 10)
print('축의금 명단 : {}'.format(wedding))
print('전체 축의금 : {}'.format(total))

print()
print()

