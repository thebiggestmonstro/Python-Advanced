

# 매직 메서드 : 클래스안에서 정의할 수 있는 Built-in 메서드
# Built-in : 파이썬 언어 자체에서 이미 정의되어 제공되는 메서드, 필요한 경우 클래스 내에서 재정의하여 사용
# 특히, 파이썬에서는 모든 자료형이 object 클래스에서 상속되므로 매직 메서드는 더더욱 중요하다

print(int)
print(float)

print(dir(int))
print(dir(float))

num = 10
print(num.__add__(10))
print(num.__mul__(10))
print(num.__bool__())