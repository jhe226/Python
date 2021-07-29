# 비시퀀스와  for문
# for문과 세트 : 랜덤 출력
for item in {'{가위}', '{바위}', '{보}'} :
    print(item)

print()

# for문과 딕셔너리
person = {
    'name' : '에밀리',
    'age' : 20
    }

for item in person :
    print(item) # key 출력
    
print()

for item2 in person :
    print(person[item2])    # 값 출력
    print(person.get(item2))

print()

# p.g 126
eng_dict = {
    'sun' : '태양',
    'moon' : '달',
    'star' : '별',
    'space' : '우주'
    }
for word in eng_dict :
    print('{}의 뜻 : {}'.format(word,eng_dict.get(word)))
