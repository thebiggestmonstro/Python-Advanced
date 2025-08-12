# 해시 테이블 : 효율적이고 빠른 검색 속도를 통해 많은 데이터를 효율적으로 관리
# 대표적인 해시 테이블인 Dictionary와 Set 모두 중복을 허용하지 않음

# immutable Dict
from types import MappingProxyType

d1 = {'Key1' : 'value1'}

# Read Only 딕셔너리
d2 = MappingProxyType(d1)
print(d1, id(d1))
print(d2, id(d2))

# 시퀀스 수정
d1['Key2'] = 'value2'
print(d1)
#d2['Key2'] = 'value2'
#print(d2)

# Set 사용
s1 = {'A', 'B', 'C', 'D', 'E'}
s2 = set(['A', 'B', 'C', 'D', 'E'])
s3 = {3}
s4 = set() # {}로 선언해선 안됨, 비어있는 set은 딕셔너리이므로 명시해야 함

# immutable set
s5 = frozenset(['A', 'B', 'C', 'D', 'E'])

# 시퀀스 수정
s1.add('F')
print(s1)
s5.add('F')
print(s5)

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# dis 모듈을 통해 파이썬 인터프리터의 실행을 바이트 코드로 볼 수 있음
from dis import dis

print(dis('{10}'))
print(dis('set([10])'))

# 후자가 전자보다 생성하는 순서가 느린것을 알 수 있음

# Set Comprehension
print({chr(i) for i in range(65, 71)})