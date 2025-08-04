from collections import namedtuple

# 네임드 튜플 선언 (1)
Point = namedtuple(typename='Point', field_names='x y')
# 네임드 튜플 선언 (2)
Point2 = namedtuple(typename='Point', field_names=['x', 'y'])
# 네임드 튜플 선언 (3)
Point3 = namedtuple(typename='Point', field_names='x, y')
# 네임드 튜플 선언 (4) - 중복된 필드명 사용
Point4 = namedtuple(typename='Point', field_names='x y x class', rename=True)

print(Point, Point2, Point3, Point4)

p3 = Point3(x=45, y=20)
p4 = Point4(10, 20, 30, 40) # rename 어트리뷰트를 통해 필드가 랜덤값에 할당됨

print(p3)
print(p4)

# 딕셔너리를 namedTuple로 변환, unpacking을 사용
tmp_dict = {'x' : 75, 'y' : 55}
p5 = Point3(**tmp_dict)
print(p5)

# 사용
print(f"{p4.x} {p4.y} {p4._2} {p4._3}")
print(f"{p5.x} {p5.y}")

x, y = p3
print(f"{x} {y}")

# 튜플 메서드의 활용
# (1) _make : 튜플 인스턴스 생성
list = [13, 17]
p6 = Point._make(list)
print(p6)

# (2) _fileds : 필드 확인
print(f"{p3._fields} {p4._fields} {p5._fields} {p6._fields}")

# (3) _asdict : OrderedDictionary 반환
print(p3._asdict())
print(p4._asdict())
print(p6._asdict())