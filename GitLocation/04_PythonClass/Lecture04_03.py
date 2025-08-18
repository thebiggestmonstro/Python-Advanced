# 파이썬의 특징

c = 40

def func_print(num):
    print(f"print : {num}")
    print(f"print : {c}")
    c = 50

def func_print2(num):
    c = 50
    print(f"print2 : {num}")
    print(f"print2 : {c}")


def func_print3(num):
    global c
    print(f"print3 : {num}")
    print(f"print3 : {c}")

def func_print4(num):
    global c
    print(f"print4 : {num}")
    print(f"print4 : {c}")
    c = 500

print(f"Before : {c}")

func_print4(100)

print(f"After : {c}")

func_print3(100)
func_print2(100)
func_print(100)

