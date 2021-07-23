# 리스트 슬라이싱

a = [1, 2, 3, 4, 5]
print(a[0:2])
print(a[2:3])
print(a[:3])
print(a[2:])
print(a[:])
print()

b = [1, 2, 3, ['b', 'c', 'd'], 4, 5]
print(b[2:5])
print(b[3][:2]) # b[3]에서 0번, 1번 인덱스 자료 출력
print()

# 리스트 연산자 : 더하기(+), 곱하기(*)
list_a = [1, 2, 3]
list_b = [4, 5, 6]

print('list_a :', list_a)
print('list_b :', list_b)

print('list_a + list_b :',list_a + list_b)  # 하나의 리스트로 합쳐진다.
print('list_a * 3 :', list_a * 3)   # list_a가 3번 반복 출력
print()

# 리스트 요소의 추가 : ***append(), insert()
list1 = [1, 2, 3]
print('list1 :', list1)
list1.append(4) # 맨 뒤에 4 삽입
print('list1 :', list1)
list1.insert(1,5)   # list[1]에 5 삽입
print('list1 :', list1)
print()

# 리스트 요소의 삭제 : del(), pop() -> 인덱스 번호로 삭제.
list2 = [0, 1, 2, 3, 4, 5]
print('list2 :', list2)
del list2[1]   # list2[1] 삭제
print('list2 :', list2)
list2.pop(2)   # list2[2] 삭제
print('list2 :', list2)
list2.pop()    # 마지막 요소 삭제
print('list2 :', list2)
print()

list3 = [0, 1, 2, 3, 4, 5, 6]
print('list3 :', list3)

del list3[3:6]  # 슬라이싱 삭제는 del()만 가능
print('list3 :', list3)
