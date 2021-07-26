# 형식을 갖춘 문자열 (문자열 포매팅)
# % 연산자 (기본 포매팅)

# p.g 58

name = 'Kai'    # 문자열
print('내 이름은 %s입니다.' %name)

height = 120.5  # 실수형
print('내 키는 %fcm입니다.' %height)

weight = 23.55  # 실수형
print('내 몸무게는 %.1fkg 입니다.' %weight)

year,month,day = 2014,8,25
print('내 생일은 %d년 %d월 %d일입니다.'%(year,month,day));
