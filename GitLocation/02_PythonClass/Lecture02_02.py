

# 매직 메서드 오버라이드를 통한 클래스간의 연산
# _변수를 사용하여 되도록 외부 접근을 막음
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f"My name is {self._name} and I am {self._age} years old"

    def __add__(self, other):
        return self._age + other._age

    def __sub__(self, other):
        return self._age - other._age

    def __ge__(self, other):
        return self._age >= other._age

    def __le__(self, other):
        return self._age <= other._age



p1 = Person("Jake", 25)
p2 = Person("Amanda", 22)

print(p1 + p2)
print(p1 - p2)
print(p1 >= p2)
print(p1 <= p2)