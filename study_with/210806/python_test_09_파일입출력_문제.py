# 파일 입출력
'''
[문제]

새로운 텍스트 파일 Text.txt를 추가하고 1부터 10까지의 수가 입력되도록 저장하여라.


[파일 출력결과]
12345678910

'''

file = open('Text.txt', 'w')
for i in range(1, 11):
    file.write(str(i))
file.close()

'''
[문제]

새로운 텍스트 파일 loop.txt를 생성하되, 파일열기모드를 추가모드로 한다. 
1부터 100까지 한 칸씩만 띄우고 모두 한 줄에 저장한다.


[파일 출력결과]
숫자 1 숫자 2 ..... 숫자 99 숫자 100 

'''
file = open('loop.txt', 'a')
for i in range(1, 101):
    data = f'숫자 {i} '
    file.write(data)
file.close()


'''
[문제]

practice.txt를 만들어 “제1의아해가무섭다고그리오.”부터 “제5의아해가무섭다고그리오.”까지
순서대로 한 줄에 하나씩 입력하여 저장하시오.
그리고 그 파일을 열어 파이썬화면에서 출력하시오


[화면 출력결과]

제1의아해가무섭다고그리오.

제2의아해가무섭다고그리오.

제3의아해가무섭다고그리오.

제4의아해가무섭다고그리오.

제5의아해가무섭다고그리오.

'''
file = open('practice.txt','w')
for i in range(1, 6):
    data = f'제{i}의아해가무섭다고그리오.\n\n'
    file.write(data)
file.close()

file = open('practice.txt','r')
lines = file.readlines()
file.close()

for i in lines:
    print(i, end = '')
print()
