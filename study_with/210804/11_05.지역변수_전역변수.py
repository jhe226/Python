# 지역변수/전역변수
'''
    지역변수 : 한정된 지역(함수)에서 사용
    전역변수 : 프로그램 전체에서 사용
               예약어 global
'''
a = 200     # 전역변수

def func1() :
    a = 10 # 지역변수
    print('func1함수에서의 a의 값 :', a)

def func2() :
    print('func2함수에서의 a의 값 :', a)

func1()
func2()

print()

# ex) 전역변수의 값을 변경하는 경우
a = 0

def f():
    global a
    a = 10

print('함수 호출 전 a :', a)
f()
print('함수 호출 후 a :', a)
