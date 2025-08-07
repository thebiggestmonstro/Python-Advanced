
# 언패킹
# 다음도 언패킹의 예시임
# a, b = b, a

# divmod : 몫과 나머지를 반환하는 함수
print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*divmod(100, 9))

# 언패킹 사용예시
x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, z, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

# 가변형 시퀀스와 불변형 시퀀스
l = [15, 20, 25]
t = (15, 20, 25)

print(l, id(l))
print(t, id(t))

# 재할당하였으므로 id가 변경
l = l * 2
t = t * 2
print(l, id(l))
print(t, id(t))

# 재할당과 달리 초기화는 가변형과 불변형이 다르게 동작함
# 가변형의 경우 값을 재설정할 수 있으므로 id가 유지되지만, 불변형의 경우 값을 재설정할 수 없으므로 id가 유지됨
l *= 2
t *= 2
print(l, id(l))
print(t, id(t))

# 즉, 가변형은 재할당하여 초기화 / 불변형은 새로 생성하여 초기화
# 따라서 값이 자주 수정되는 경우 가변형에 저장하는 것이 유리함

# sort vs sorted
# 사용할 수 있는 인자 : reverse=False, key=len, key=str.lower, key=func ...
