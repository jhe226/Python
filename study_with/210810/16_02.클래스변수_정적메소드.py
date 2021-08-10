# 클래스 변수
'''
     클래스 안에서 공간이 할당된 변수
     여러 인스턴스가 클래스 변수 공간을 함께 사용
'''
class Car :    # 클래스 정의
     cnt  = 0  # 클래스 변수
     def __init__(self, name, speed):   # 생성자
          self.name = name    # 인스턴스 변수(속성)
          self.speed = speed
          Car.cnt += 1   # 클래스 변수에 1씩 증가

my_car = Car('벤츠', 0)
print(f'{my_car.name}의 현재 속도 : {my_car.speed}km, 생산된 자동차 수 : {Car.cnt}대')

bro_car = Car('소나타', 30)
print(f'{bro_car.name}의 현재 속도 : {bro_car.speed}km, 생산된 자동차 수 : {Car.cnt}대')

sis_car = Car('BMW', 60)
print(f'{sis_car.name}의 현재 속도 : {sis_car.speed}km, 생산된 자동차 수 : {Car.cnt}대')

print()
print()

# 클래스 메소드
'''
     클래스 변수를 사용하는 메소드
     인스턴스 없어도 호출 가능
     매개변수 cls 사용
     @classmethod 데코레이터로 표시
'''

class Korean:
     country = '한국'
     @classmethod
     def trip(cls, country):
          if cls.country == country:
               print('국내여행입니다.')
          else:
               print('해외여행입니다.')
               
Korean.trip('한국')
Korean.trip('미국')
Korean.trip('중국')

print()
print()

# 정적 메소드

class Korean:
     country = '한국'
     @staticmethod
     def slogan():       # 정적 메소드
          print('Imagine your Korea')
Korean.slogan()

print()
print()

# p.g 282
class Bag:
     cnt = 0
     def __init__(self):
          Bag.cnt += 1
     @classmethod
     def sell(cls):
          cls.cnt -= 1

     @classmethod
     def remain_bag(cls):
          return cls.cnt
     
print('현재 가방 : {}개'.format(Bag.remain_bag()))
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print('현재 가방 : {}개'.format(Bag.remain_bag()))
bag1.sell()
bag2.sell()
print('현재 가방 : {}개'.format(Bag.remain_bag()))

print()
print()  
