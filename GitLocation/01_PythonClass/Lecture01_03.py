
class Person():
    '''
    Represent Human
    '''

    # 클래스 static 변수
    person_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.person_count += 1

    def __del__(self):
        self.person_count -= 1
        Person.person_count -= 1

    def __str__(self):
        return f"name : {self.name} / age : {self.age}"

    # 사용자 정의 함수
    def printInfo(self):
        print(f"My name is {self.name}. I am {self.age} years old.")

p1 = Person("John", 19)
print(p1.person_count)
p2 = Person("Kwon", 19)
print(p2.person_count)
p3 = Person("Park", 19)
print(p3.person_count)

# self 예약어를 통해 어트리뷰트를 초기화하지 않은 클래스에서의 멤버 함수 사용
Person.printInfo(p1)
p2.printInfo()

# 클래스 변수에 대한 접근
print(p1.person_count)
print(Person.person_count)

del p1
print(Person.person_count)
del p2
print(Person.person_count)
del p3
print(Person.person_count)