# 키워드 인수
'''
    각각의 매개변수가 어던 용도이지 알기 어려울 때 사용
'''

def info(name, age, address):
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)

    print()

info('라이언', 20, '대구')   # 일반적인 호출방식
info(name = '어피치', age = 30, address = '서울')    # 키워드 지정
info(age = 40, address = '부산', name = '무지')
