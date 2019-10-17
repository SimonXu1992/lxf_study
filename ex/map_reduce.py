from functools import reduce
"""
输入英文名字,变成首字母大写,其他字母小写的标准格式
"""
def normalize(name):
	return name[0].upper()+name[1:].lower()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

"""
请编写一个prod()函数，可以接受一个list并利用reduce()求积
"""

def prod(L):
    return reduce(lambda x,y:x*y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

"""
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
"""


def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    n = s.index(".")
    s1 = list(map(int, s[:n]))
    s2 = list(map(int, s[n+1:]))
    zhengshu = reduce(lambda x,y:10*x+y, s1)
    xiaoshu = reduce(lambda x,y:10*x+y, s2)/(10**(len(s2)))
    return zhengshu+xiaoshu

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')