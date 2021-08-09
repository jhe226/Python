# 객체 지향 프로그래밍 (Object-Oriented Programming, OOP)
'''
    복잡한 문제를 작게 나누어 객체(object)를 만들고,
    객체를 조합하여 문제를 해결하는 방식
    복잡한 문제를 처리하는데 유용하며,
    기능을 개선하고 발전시킬 때에도 해당 클래스만 수정하면 되므로
    유지보수에 효율적

    클래스(class) : 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계도
                    (과자틀, 붕어빵틀에 비유)

    객체(object) : 각각의 객체마다 고유의 특성을 가짐.
                   (붕어빵 틀에서 만들어낸 붕어빵에 비유)
                   파이썬에서는 문자, 숫자, 리스트, 딕셔너리, 함수 등 모두 객체이다.

    인스턴스(instance) : 특정 객체가 어떤 클래스의 객체인지 관계 위주로 설명할 때
                         사용 클래스와 연관지어서 객체를 말할 때 인스턴스라고 한다.

    메서드(method) : 클래스 안에서 구현된 함수


    <형식>
    class 클래스 이름 :    # 파이썬에서는 클래스 이름을 대문자로 시작
        def 메서드 이름(self, 매개변수):   # 메서드를 호출 한 객체가 자동으로 전달되는 매개변수 --> self
            self.속성 = 값

    인스턴스 이름 = 클래스 이름()   # 인스턴스(객체) 생성
    인스턴스 이름.메서드 이름()     # 메서드 호출(함수 호출)
    
'''

# 인스턴스 변수와 인스턴스 메서드

class Person:
    def who_am_i(self, name, age, tel, address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

boy = Person()  # boy 객체(인스턴스) 생성
boy.who_am_i('john', 15, '123-4567', 'toronto')  # 메서드(함수) 호출
print(boy.name)
print(boy.age)
print(boy.tel)
print(boy.address)
print()

# p.g 267
class Computer:
    def set_space(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd
        
    def hardware_info(self):
        print('CPU = {}'.format(self.cpu))
        print('RAM = {}GB'.format(self.ram))
        print('VGA = {}'.format(self.vga))
        print('SSD = {}GB'.format(self.ssd))


desktop = Computer()
desktop.set_space('i7', 16, 'GTX1060', 512)
desktop.hardware_info()

notebook = Computer()
notebook.set_space('i5', 8, 'MX300', 256)
notebook.hardware_info()

print()
print()

# p.g 269
class Calculator:
    def input_expr(self):
        expr = input('수식을 입력하세요 >> ')
        self.expr = expr
    def calculate(self):
        return eval(self.expr)

calc = Calculator()
calc.input_expr()
print('수식 결과는 {}입니다.'.format(calc.calculate()))
