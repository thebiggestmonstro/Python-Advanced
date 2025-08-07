# sort vs sorted
# 사용할 수 있는 인자 : reverse=False, key=len, key=str.lower, key=func ...
# 두 함수의 차이점
# 전자 : 정렬 후 객체 직접 변경 -> 원본을 수정
# 후자 : 정렬 후 새로운 객체로 반환 -> 원본을 수정하지 않음

humans = ["Kim", "Park", "Choi", "Kwon", "Han"]
print(f"Use sorted() : {sorted(humans)}")
print(f"Use sorted() : {sorted(humans, reverse=True)}")
print(f"Use sorted() : {sorted(humans, key=len)}")
print(f"Use sorted() : {sorted(humans, key=lambda x : x[-1])}")
print(humans)

print(f"Before sort() : {humans.sort()} / After sort() : {humans}")
print(f"Before sort() : {humans.sort(reverse=True)} / After sort() : {humans}")
print(f"Before sort() : {humans.sort(key=len)} / After sort() : {humans}")
print(f"Before sort() : {humans.sort(key=lambda x : x[-1])} / After sort() : {humans}")