# p.g 160
# 01.
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
for index, color in enumerate(rainbow, start = 1):
    print(f'무지개의 {index}번째 색은 {color}입니다.')

print()

# 02.
exam = []
print('점수를 입력하세요. 더 이상 입력할 점수가 없으면 음수를 아무거나 입력하세요.')
while True :
    score = float(input('점수 입력 >>> '))
    if score > 0:
        exam.append(score)
        continue
    else :
        break
print('평균 = {}, 최대 = {}, 최소 = {}'.format(sum(exam)/len(exam), max(exam), min(exam)))

print()
