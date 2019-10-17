def _odd_iter():
    """
    构造一个从3开始的无限序列
    :return:
    """
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    """筛选函数"""
    return lambda x: x % n >0


def primers():
    """定义一个生成器，不断返回下一个素数"""
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


if __name__ == '__main__':
    for n in primers():
        if n<1000:
            print(n)
        else:
            break