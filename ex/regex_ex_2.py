"""版本二可以提取出带名字的Email地址：

<Tom Paris> tom@voyager.org => Tom Paris
bob@example.com => bob
"""
# -*- coding: utf-8 -*-
import re

# re_name_of_email = re.compile(r'^<?(\w+\s*\w*)>?\s*\w*@\w+\.org$]')
re_name_of_email = re.compile(r'^<?([\w]+\s*[\w]*)>?\s*[\w]*@[\w]+\.org$')


def name_of_email(addr):
    if re_name_of_email.match(addr):
        return re_name_of_email.match(addr).group(1)
    return None


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')