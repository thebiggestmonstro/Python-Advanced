# 클로저를 사용하는 이유
# 1) 변수에 대한 관리와 책임을 Closure를 통해 변수에 접근하는 방식으로 명확히 할 수 있음
# 2) Closure에 의해 변수에 접근하므로 변수간의 불필요한 충돌을 막을 수 있음
# 3) Closure의 로직을 임의로 조정하여 사용환경(Context)에 맞게끔 설정할 수 있음

# 클로저의 특징
# -> 클로저의 Inner는 자신을 둘러싼 함수 스코프의 상태값을 참조하는데, 함수가 메모리에서 제거되어도 값이 유지됨

class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        return sum(self._series) / len(self._series)

ex1 = Averager()

print(ex1(10))
print(ex1(100))
print(ex1(1000))

print()
print()

# 위의 예시를 클로저로 변경

def outer_average():
    n = 0
    i = 0

    def inner_average(num):
        nonlocal n, i
        n += num
        i += 1
        return n / i

    return inner_average


avg = outer_average()

print(avg(10))
print(avg(100))
print(avg(1000))