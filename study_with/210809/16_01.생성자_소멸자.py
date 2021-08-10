# 생성자(constructure)
'''
    객체의 초기값을 설정해야 할 필요가 있을 때 사용
    객체가 생성될 때 자동으로 호출되는 메서드
    __init__ 사용

    스페셜 메서드(매직 메서드) : 파이썬에서 자동으로 호출해주는 메서드
                                앞뒤로 __가 붙은 메서드

    <형식>
    class 클래스 이름:
        def __init__(self):    # 생성자
            self.속성 = 값
'''

class Candy : # 클래스 정의
    def set_info(self, shape, color) :      # 인스턴스 메서드 정의
        self.shape = shape
        self.color = color

satang = Candy()    # 객체(인스턴스) 생성
satang.set_info('circle', 'brown')  # 인스턴스 메서드 호출
print(satang.shape)
print(satang.color)
print()

class Candy2 : # 클래스 정의
    def __init__(self, shape, color) :      # 인스턴스 메서드 정의
        self.shape = shape
        self.color = color

satang1 = Candy2('circle', 'brown')
print(satang1.shape)
print(satang1.color)
print()

# 소멸자
class Sample :
    def __del__(self):
        print('인스턴스가 소멸되었습니다.')
s = Sample()
del s
print()

# p.g 276
class USB:
    def __init__(self, capacity):
        self.capacity = capacity
    def info(self):
        print('{}GB USB'.format(self.capacity))
usb = USB(64)
usb.info()
print()

# p.g 277
class Service:
    def __init__(self, service):
        self.service = service
        print('{} Service가 시작되었습니다.'.format(self.service))
                
    def __del__(self):
        print('{} Service가 종료되었습니다.'.format(self.service))

service = Service('길 안내')
del service
print()
