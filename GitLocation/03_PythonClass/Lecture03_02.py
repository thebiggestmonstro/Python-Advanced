# 리스트 사용시의 주의사항
m1 = [['~'] * 3 for _ in range(3)]
m2 = [['~'] * 3] * 3

print(m1)
print(m2)

# 값을 수정
m1[0][1] = 'X'
m2[0][1] = 'X'

print(m1)   # 각각 다른 시퀀스 객체가 생성됨
print(m2)   # 같은 시퀀스 객체를 복사함

print([id(i) for i in m1])
print([id(i) for i in m2])