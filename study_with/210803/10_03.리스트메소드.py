# 리스트 메소드
# extend() : 확장. 리스트를 서로 더할 수 있다.
my_list = ['apple', 'banana']
my_list.extend(['cherry', 'mango'])
print(my_list)
print()

# insert() : 특정 인덱스에 데이터 추가
my_list = ['apple', 'banana']
my_list.insert(0, 'cherry')
print(my_list)
print()

# clear() : 리스트에 저장된 모든 요소 삭제
my_list = ['apple', 'banana']
my_list.clear()
print(my_list)
print()

# pop() : 마지막 요소 반환 후 제거
my_list = ['apple', 'banana']
item = my_list.pop()
print(item)
print(my_list)
print()

# remove() : 특정 요소 직접 입력하여 제거
my_list = ['apple', 'banana', 'cherry', 'mango']
my_list.remove('mango')
print(my_list)
print()

# p.g 177
a_list = ['above', 'cookie', 'app', 'about', 'admire', 'bisket', 'apple', 'april']
for i, item in enumerate(a_list):
    if item.find('a') == -1:
        print('{} 제거됩니다.'.format(a_list.pop(i)))
print(a_list)
print()
