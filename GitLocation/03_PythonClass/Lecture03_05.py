
# 해시테이블 : Key에 Value를 저장하는 구조, 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# Key 값을 해싱 함수에 인자로 사용하여 해시 주소를 반환함, 반환받은 해시 주소를 통해 Key에 대한 Value에 접근
# 대표적으로 Dictionary가 해시 테이블의 예시

# 예시를 통한 해시 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
#print(hash(t2))

# 즉, 해시는 Immutable한 경우에서만 사용가능

source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k1', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# setdfault 함수를 사용하지 않고 튜플을 딕셔너리로 전환
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# setdefault 함수를 사용하여 튜플을 딕셔너리로 전환
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)