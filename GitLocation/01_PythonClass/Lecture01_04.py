# 클래스 기반 메서드 심화
# Class Method
# Instance Method
# Static Method

class Person():
    '''
    Represent Human
    '''

    # static 변수(모든 인스턴스가 공유)
    personCount = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name : {self.name} / age : {self.age}"

    # self 예약어를 사용하는 인스턴스 메서드
    # self : 클래스의 인스턴스(객체) 자신을 가리키는 예약어
    # 되도록 인스턴스로서 호출
    def printPersonInfo(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


    # 클래스 메서드는 @classmethod 데코레이터를 사용
    # 클래스를 인자로 사용
    # 클래스의 static 변수를 설정하는 용도
    # 되도록 클래스로서 호출
    @classmethod
    def setPersonCount(cls, count):
        if count <= 0:
            print('count must be more than 0')
            return
        cls.personCount = count
        print('PersonCount was set')

    # static 메서드는 가급적 인자를 받지 않음
    # @staticmethod 데코레이터를 사용하여 정의
    # 상황에 맞춰 유연하게 클래스나 인스턴스로 호출
    @staticmethod
    def getChildClass(inst):
        if isinstance(inst, Person):
            print(f"{inst.name} is Person`s Instance")
        else:
            print(f"{inst} is not Person`s Instance")



p1 = Person("John", 19)
p2 = Person("Kwon", 19)
p3 = Person("Park", 19)

p1.printPersonInfo()

print(f"Before : {p1.personCount}")
Person.setPersonCount(2)
print(f"After : {p1.personCount}")

Person.getChildClass(p3)
Person.getChildClass(object)
p2.getChildClass(p1)