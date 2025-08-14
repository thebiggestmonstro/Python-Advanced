# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1) 런타임 초기화
# 2) 변수에 할당 가능
# 3) 일급 함수를 다른 함수의 인수로 전달 가능
# 4) 일급 함수를 다른 함수의 반환값으로 사용 가능

# 함수를 인수로 전달 및 함수로 결과 반환 = High-order function
# map, filter, reduce

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

# 함수 객체
func = factorial

print([func(i) for i in range(1, 6) if i % 2])
print(list(map(func, filter(lambda x : x % 2, range(1, 6)))))

# reduce 함수 - 모듈로 사용
from functools import reduce
from operator import add

print(reduce(add, range(1, 11)))

# reduce 함수 - 람다로 구현
print(reduce(lambda x, y : x + y, range(1, 11)))

# callable : 호출 연산자로서 메서드 형태로 호출 가능한지 확인
print(callable(str), callable(add), callable(func), callable('Hello'))

# Closure(클로저) : 함수가 정의될 때의 환경을 기억하고, 외부 함수가 종료된 후에도 해당 환경에 접근할 수 있는 내부 함수
# 사용 목적
# 1) 데이터를 캡슐화하여 정보의 은닉성을 높일 수 있음
# 2) 상태를 유지할 수 있음
# 3) 데코레이터를 구현하는 데 유용함
def outer(x):
    i = 0

    # closure
    def inner(y):
        nonlocal i
        i += 1
        print(f"No.{i} value of d : {x + y}")
    return inner

in_test = outer(5)
in_test(5)
in_test(10)
in_test(15)

# partial 사용법 : 인수를 고정하여 콜백 함수로 사용
from operator import mul
from functools import partial

print(mul(10, 10))
five = partial(mul, 5)
print(five(5))
print(five(10))
six = partial(five, 6)
print(six())