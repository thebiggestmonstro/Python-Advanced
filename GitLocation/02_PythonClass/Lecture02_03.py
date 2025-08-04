
class Vector(object):
    def __init__(self, *arg):
        '''
        Create Instance with this format : Vector(x, y)
        '''
        if len(arg) <= 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = arg

    def __repr__(self):
        '''
        return Info about Vector class
        '''
        return f"Vector({self._x}, {self._y})"

    # 벡터의 합
    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    # 스칼라곱
    def __mul__(self, num):
        return Vector(self._x * num, self._y * num)

    # 벡터의 원점 여부 확인
    def __bool__(self):
        return bool(max(self._x, self._y) or min(self._x, self._y))


v1 = Vector(5, 4)
v2 = Vector(6, 3)
v3 = Vector()
v4 = Vector(-3, 0)
v5 = Vector(0, -5)
v6 = Vector(3, 3)

print(v1 + v2)
print(v2 * 3)
print(v3)
print(bool(v3))
print(bool(v4))
print(bool(v5))
print(bool(v6))