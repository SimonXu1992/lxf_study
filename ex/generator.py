# python3
# 非常重要的一点列表是引用类型
# import copy
# def triangles():
#     """
#     使用copy库
#     :return:
#     """
#     L = []
#     while True:
#         if (len(L) < 2):
#             L.append(1)
#
#         else:
#             length = len(L)
#             for i in range(length - 1):
#                 L[i] = L[i] + L[i + 1]
#             L[length - 1] = 1
#             L.insert(0, 1)
#         yield copy.copy(L)
#
def triangles():
    """
    使用列表生成器
    :return:
    """
    L = []
    while True:
        if (len(L) < 1):
            L.append(1)

        else:
            length = len(L)
            L = [ L[i] + L[i + 1] for i in range(length - 1)]

            L = [1] + L + [1]
        yield L

#
# def triangles():
#     """最优重新为L赋值，并使用列表生成器，最优"""
#     L = [1]
#     while True:
#         yield L
#         L = [1]+[L[i] + L[i+1] for i in range(len(L)-1)]+[1]
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    # print(results)
    n = n + 1
    if n == 10:
        break
print(results)
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
