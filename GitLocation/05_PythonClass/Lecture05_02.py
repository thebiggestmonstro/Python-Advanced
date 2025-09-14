
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stop Iteration')
        self._idx += 1
        return word

    def __repr__(self):
        return f"WordSplit {self._text}"

ex1 = WordSplitter("Hello Python")
print(next(ex1))
print(next(ex1))

# 클래스로 구현한 Iterator 예제를 Generator로 변경
# 1) 지능형 리스트 / 딕셔너리 / 집합과 같이 데이터양이 증가하면 메모리에 부하를 주는 자료구조에 탁월함
# 2) 단위 별로 실행가능한 코루틴 구현과 연동
# 3) 작은 메모리 조각 사용

class WordSplitterWithGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word
        return

    def __repr__(self):
        return f"WordSplitWithGenerator {self._text}"

ex2 = WordSplitterWithGenerator("Hello Python")
ex3 = iter(ex2)
print(next(ex3))
print(next(ex3))
