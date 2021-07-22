# 문자열 인덱싱

'''
[문제]
출력결과를 참고하여 문자열 인덱싱으로 한글자씩 출력해보자.

string = 'PYTHON'

[출력결과]
P
Y
N
N
H

'''
string = 'PYTHON'
print(string[0])
print(string[1])
print(string[5])
print(string[5])
print(string[3])
print()

# 문자열 슬라이싱
'''
[문제]
문자열 슬라이싱으로 출력결과와 같도록 출력해보자.

mystr = 'GOOD NIGHT'

[출력결과]
OO
 NIGHT
GH
OD

'''
mystr = 'GOOD NIGHT'
print(mystr[1:3])
print(mystr[4:])
print(mystr[-3:-1]) # 또는 print(mystr[7:9])
print(mystr[2:4])
print()
