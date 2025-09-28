# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램에서 여러 일을 동시에 수행
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 다중 프로그램에서 여러 일을 동시에 수행(속도 상승)

# 병행성 예시
def gen_ex1():
    print('Start')
    yield 'First Step'
    print('Continue')
    yield 'Second Step'
    print('End')

tmp = iter(gen_ex1())

# print(next(tmp))
# print(next(tmp))
# print(next(tmp))

# for 문에서는 StopIteration 예외처리를 자동으로 제공
for t in gen_ex1():
    print(t)

# Generator 사용에 있어서 유용한 함수
import itertools

# count 함수 : 인자로 시작값 / 증감값, 값이 무한대로 증가함
gen1 = itertools.count(1, 2.5)
print(next(gen1))
print(next(gen1))

# takewhile 함수 : 조건을 만족할때까지 generator 사용
gen2 = itertools.takewhile(lambda n : n < 15, itertools.count(1, 3))
for v in gen2:
    print(v)

# filterfalse 함수 : 조건을 만족하지 않을때까지 generator 사용
gen3 = itertools.filterfalse(lambda n : n < 3, [1, 2, 3, 4, 5])
for v in gen3:
    print(v)

# accumulate 함수 : 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 11)])
for v in gen4:
    print(v)

# chain 함수 : 연결 함수 (1)
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print(list(gen5))

# chain 함수 : 연결 함수 (2)
gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))

# product 함수 : 개별 튜플로 분리
gen7 = itertools.product(enumerate('ABCDE'))
print(list(gen7))

# repeat 인자를 설정하여 개별 분리되는 튜플 내부의 데이터 개수를 설정
gen8 = itertools.product(enumerate('ABCDE'), repeat=2)
print(list(gen8))

# groupby 함수 : 그룹화
gen9 = itertools.groupby('AAABBBCCCDDD')
for chr, group in gen9:
    print(chr, ' : ', list(group))

















