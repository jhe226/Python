# 세트(집합) : 순서X -> 인덱싱, 슬라이싱X. 중복 값 저장X -> 중복 제거용
s1 = {1, 2, 3}
print('세트 s1 :', s1)

# 요소 1개 추가 : add()
s1.add(4)
print('세트 s1 :', s1)

# 요소 여러 개 추가 : update()
s1.update([5, 6, 7])    # 리스트 형태로 삽입
print('세트 s1 :', s1)

# 특정 요소 제거 : remove(), discard()
s1.remove(3)
print('세트 s1 :', s1)
s1.discard(5)
print('세트 s1 :', s1)
s1.discard(0)
print('세트 s1 :', s1)

# remove()  vs  discard()
'''
    remove(a) : a가 없으면 오류 발생
    discard(a) : a가 없어도 오류X
'''
