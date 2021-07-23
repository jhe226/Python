# 딕셔너리
dic = {'name' : '홍길동', 'birth' : '1212'}
print('딕셔너리 dic :', dic)
print()

# 특정 값 출력
print(dic['name'])  # 해당 키를 적는다.
print()

# 딕셔너리 값 수정
dic['name'] = '라이언'
print('딕셔너리 dic :', dic)
print(dic['name'])
print()

# 딕셔너리 쌍 추가하기
dic['address'] = 'Daegu'    # 해당하는 키가 없으면 추가됨.
print('딕셔너리 dic :', dic)
print()

# key 리스트 만들기
print(dic.keys())   # 키 부분만 따로 모은 것
print()

# 값(value) 리스트 만들기
print(dic.values()) # 값 부분만 따로 모은 것
print()

# 딕셔너리 쌍 삭제
del dic['address'] # address에 해당하는 키와 값 삭제
print('딕셔너리 dic :', dic)
print()

# items 함수를 이용한 쌍 얻기
print(dic.items()) # 쌍이 튜플 형식으로 묶임
print()

# 키와 값 모두 지우기
dic.clear()
print('딕셔너리 dic :', dic)
print()
