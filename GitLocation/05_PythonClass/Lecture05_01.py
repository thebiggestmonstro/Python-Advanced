# generator : iterator를 생성하는 함수
# iterator : 반복가능(iterable)한 객체

# 파이썬에서 iterable한 타입
# collections 모듈의 요소들 / text file / Sequence들

text = "qwertyuooo[asdjknzvnm,xc"
print(dir(text))
print(text.__iter__())


# iter 함수를 사용하여 iterable한 객체를 생성
# next 함수를 사용하여 iterable한 객체로부터 데이터 추출 / 한번 추출된 데이터는 사용불가
words = iter(text)
while True:
    try:
        print(next(words))
    except StopIteration:
        break

# iterable한지 확인하는 방법
from collections import abc

print(dir(text))
print(hasattr(text, '__iter__'))
print(isinstance(text, abc.Iterable))