# continue문

# ex) 0~ 10 사이의 수 중 홀수만 출력
a = 0
while a < 10 :
    a = a + 1   # a += 1
    if a % 2 == 0 :
        continue
    print(a)

print()

# p.g 139
fruits = ['사과 ', '감귤']
cnt = 3

while cnt > 0:
    fruit = input('어떤 과일을 저장할까요? >>> ')
    if fruit in fruits:
        print('동일한 과일이 있습니다.')
        continue
    fruits.append(fruit)
    cnt -= 1
    print('입력이 {}번 남았습니다.'.format(cnt))
print('5개 과일은 {}입니다.'.format(fruits))

print()

# p.g 140

cnt = 0
total = 0
while cnt < 5:
    n = int(input('{}번째 정수를 입력하세요 >>> '.format(cnt+1)))
    if n <= 0 :
        print('0 이하의 정수는 처리할 수 없습니다.')
        continue
    total += n
    cnt += 1
print('입력된 5개 양수의 총합은 {}입니다.'.format(total))
print()

