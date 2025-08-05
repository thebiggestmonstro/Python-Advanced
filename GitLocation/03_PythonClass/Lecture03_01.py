# 시퀀스형
# Container 시퀀스 : 서로 다른 자료형을 저장할 수 있음 예시) list, tuple, dictionary, collections.deque
# Flat 시퀀스 : 단일 자료형만 저장할 수 있음 에시) str(문자열), bytes, bytearray, array.array, memoryview
# mutable 시퀀스 : list, bytearray, array.array, memoryview, collections.deque
# immutable 시퀀스 : tuple, str, bytes

# 리스트와 튜플 고급
# 지능형 리스트(Comprehending Lists)
chars = "abcdefghijklmnopqrstuvwxyz"

code_list = [ord(s) for s in chars]
print(code_list)

# 지능형 리스트(Comprehending Lists) + map + tuple
code_list2 = list(filter(lambda x : x % 2 == 0, map(ord, chars)))
print(code_list2)

# Generator 생성 -> ()(소괄호)로 컴프리헨션 코드를 감싸서 생성
import array

tuple_generator = (ord(s) for s in chars)
print(tuple_generator)
print(type(tuple_generator))
print(next(tuple_generator))
print(next(tuple_generator))

# array 사용
array_generator = array.array('I', (ord(s) for s in chars))
print(array_generator)
print(type(array_generator))
print(array_generator.tolist())

# Generator 사용예제
for s in (f"{w + str(n)}" for w in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)


