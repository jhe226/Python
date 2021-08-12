# 클래스 상속
'''
     어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만든 것
     
     <형식>
     class 클래스 이름(상속할 클래스 이름):
     class 서브 클래스(슈퍼 클래스):
     class 자식 클래스(부모 클래스):
     
'''
class Person:  # 슈퍼 클래스(부모클래스)
     def __init__(self, name): 
          self.name = name
     
     def eat(self, food):
          print(self.name+'가'+food+'를 먹습니다.')

class Student(Person):   # 서브 클래스 (자식 클래스)
     def __init__(self, name, school):  # 서브 클래스 생성자
          super().__init__(name)   # 슈퍼 클래스 생성자
          self.school = school

     def study(self):    # 인스턴스 메소드
          print(self.name+'는'+self.school+'에서 공부를 합니다.')

potter = Student('해리포터', '호그와트')
potter.eat('감자')
potter.study()

print()
print()

# p.g 286
class Coffee:
     def __init__(self, bean):
          self.bean = bean
     def coffee_info(self):
          print('원두: {}'.format(self.bean))

class Espresso(Coffee):
     def __init__(self, bean, water):
          super().__init__(bean)
          self.water = water

     def espresso_info(self):
          super().coffee_info()
          print('물 : {}ml'.format(self.water))

coffee = Espresso('콜롬비아', 30)
coffee.espresso_info()

print()
print()

# 메소드 오버라이딩(재정의)
'''
     부모 클래스에 있는 메소드를 동일한 이름으로 다시 만드는 것
     부모 클래스의 메서드 대신 오버라이딩(덮어쓰기)한 메소드가 호출된다
     프로그램에서 어떤 기능이 같은 메소드 이름으로 계속 사용되어야 할 때 활용
'''
class Car: # 부모클래스(슈퍼클래스)
     def __init__(self, speed): # 생성자
           self.speed = speed

    def upSpeed(self, value): # 인스턴스 메서드
        self.speed += value
        print(f'현재 속도(부모 클래스) : {self.speed}')
          
class Sedan(Car) :       # 서브 클래스
     def __init__(self, speed, name):
          super().__init__(speed)
          self.name = name

     def upSpeed(self, value):     # 메소드 오버라이딩
          self.speed += value
          if self.speed > 150:
               self.speed = 150
          print(f'현재 속도(서브 클래스) : {self.speed}')

car1 = Car(0)
car1.upSpeed(200)

car2 = Sedan(10, '세단')
car2.upSpeed(200)


print()
print()
