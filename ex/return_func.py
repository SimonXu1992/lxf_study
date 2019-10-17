"""
利用闭包返回一个计数器函数，每次调用它返回递增整数.
"""

s=0

def createCounter():
    def counter():
        global s
        s += 1
        return s

    return counter


if __name__ == '__main__':
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    s=0
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')