
class Person():
    '''
    Represent Human
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name : {self.name} / age : {self.age}"

p1 = Person("John", 19)
p2 = Person("Kwon", 19)
p3 = Person("Park", 19)

# id 함수를 이용한 인스턴스의 아이디 출력 : self는 클래스의 인스턴스 자기자신을 의미, 어트리뷰트를 설정하기 위해 사용
print(id(p1))
print(id(p2))
print(id(p3))

# dir 메서드를 사용하여 인스턴스의 어트리뷰트를 리스트로 출력
print(dir(p1))
print(dir(p2))

# __dict__ 매직 메서드를 사용하면 불필요한 정보는 생략하면서 어트리뷰트의 값까지 확인할 수 있음
print(p1.__dict__)
print(p2.__dict__)

# __doc__ 매직 메서드를 사용하여 클래스의 설명 출력
print(p1.__doc__)
print(p2.__doc__)

# __class__ 매직 메서드를 사용하여 인스턴스의 클래스 확인
print(p1.__class__)
print(p2.__class__)

print(id(p1.__class__) == id(p2.__class__))