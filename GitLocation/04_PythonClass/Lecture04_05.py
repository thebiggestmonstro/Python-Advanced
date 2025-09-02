
# 데코레이터 : 함수와 메서드의 기능을 쉽게 수정하기 위한 수단
# 또는 함수를 파라미터로 받아서 함수를 반환하는 함수

# 데코레이터의 장점
# 1) 코드의 가독성 및 명확성 향상
# 2) 높은 재사용성 및 모듈화 -> 공통의 기능을 수행하는 경우 특히 유리함
# 3) 유지보수 용이성 증대
# 4) 기존의 코드를 안전하게 수정

# 데코레이터의 단점
# 1) 코드의 복잡성 증가
# 2) 특정 기능의 함수는 단일 함수가 더 유리함
# 3) 디버깅이 불편함

# 데코레이터를 사용한 타이머 예시
import time
def action_timer(func):
    def set_timer(*args):
        # 함수를 호출한 시간 / 함수 수행 결과 / 함수를 실행한 시간
        start_time = time.perf_counter()
        result = func(*args)
        finish_time = time.perf_counter()

        # 순수하게 함수를 수행한 시간 / 함수의 이름 / 함수의 인자
        execute_time = finish_time - start_time
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)

        # 출력문
        print(f"함수 : {name}에 인자를 {arg_str}으로 하여 최종 {result}가 반환 /  {execute_time:.5f}초 만큼 실행")
        return result
    return set_timer


# 데코레이터의 인자로 사용하는 경우, 데코레이터를 어노테이션으로 지정
@action_timer
def sum_all(*args):
    time.sleep(10)
    return sum(args)

sum_all(50, 40, 30)