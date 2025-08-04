
# 일반적인 튜플을 이용한 두 점 사이의 거리 구하기
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_len1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_len1)

# 네임드 튜플을 이용한 두 점 사이의 거리 구하기
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple(typename='Point', field_names='x y')

# 네임드 튜플 인스턴스 선언
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

l_len2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(l_len2)