# 표준출력

# 이스케이프 문자
'''
    프로그래밍할 때 사용할 수 있도록
    미리 정의해둔 문자 조합
    출력물을 보기 좋게 정렬하는 용도
'''

# p.g 53
print('Hello \'World\'')
print("Hello \"World\"")
print('*\n**\n***')
print('이름\t연락처')
print('제시카\t02-123-4567')
print('마틴\t010-8765-1234')
print()

# p.g 55
print('재미있는', '파이썬')
print('Python', 'Java', 'C', sep = ', ')
print()
print('영화 타이타닉')
print('평점', end = ':')
print('5점')

fos= open('sample.py',mode = 'wt')
print('print("Hello World")', file=fos)
fos.close()
print()
