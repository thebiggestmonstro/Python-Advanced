# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1) 런타임 초기화
# 2) 변수에 할당 가능
# 3) 일급 함수를 다른 함수의 인수로 전달 가능
# 4) 일급 함수를 다른 함수의 반환값으로 사용 가능

# 함수 객체
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

class A:
    pass


print(factorial(5))
print(type(factorial), type(A))
print(dir(factorial))
print(set(sorted(dir(factorial))) - set(sorted((dir(A)))))  # 클래스와 다르게 함수만이 갖고 있는 속성 출력

# 함수 객체
func = factorial
print(func)
print(func(10))
print(list(map(func, range(1, 10))))

# 함수를 인수로 전달 및 함수로 결과 반환 = High-order function
