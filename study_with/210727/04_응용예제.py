# p.g 85
# 01.
a = int(input('10 ~ 99 사이의 정수를 입력하세요 >>> '))
print('십의 자리 : {}'.format(int(a/10)))
print('일의 자리 : {}'.format(a%10))
print()

# 02.
sec = int(input('초를 입력하세요 >>> '))
print('변환 결과는 {}시간 {}분 {}초입니다'.format(int(sec/3600), int((sec-3600)/60),int((sec-3600)%60)))
print()

# 03.
num= int(input('4자리 사원번호를 입력하세요 >>> '))
time = ('오후')if(int(num%10)>12)else('오전')
print('근무시간은 {}입니다.'.format(time))
print()

#p.g 86
# 04.
print('한 박스에 20개의 라면을 담을 수 있습니다.\n라면의 개수를 입력하시면 필요한 박스 수를 알려드립니다.')
a = int(input('라면의 개수를 입력하세요 >>> '))
box = int(a/20) + 1
print('{}개 라면을 담으려면 {}박스가 필요합니다.'.format(a, box))
print()

# 05.
ko = int(input('국어 점수를 입력하세요 >>> '))
en = int(input('영어 점수를 입력하세요 >>> '))
math = int(input('수학 점수를 입력하세요 >>> '))
avr = (ko + en + math)/3
result = ('합격')if(avr>=80)else('불합격')
print(f'평균은 {avr:.1f}점이고, 결과는 {result}입니다.')


