

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__ 매직 메서드를 구현하면 인스턴스의 메모리 정보를 출력하지 않고,
    # 정의한 문자열의 형태로 클래스의 정보를 출력함
    #def __str__(self):
    #    return f"name : {self.name} / age : {self.age}"

    # 동일한 역할을 수행하는 __repr__ 매직 메서드도 존재한다
    # 차이점은 전자의 경우 사용자의 편의성을 위해 사용하고, 후자의 경우 유의미한 정보를 제공하기 위해 사용한다
    #def __repr__(self):
    #    return f"name : {self.name} / age : {self.age}"

p1 = Person("John", 19)
print(p1)

# __dict__ 매직 메서드를 사용하여 인스턴스의 어트리뷰트를 딕셔너리 형태로 출력할 수 있다
print(p1.__dict__)
