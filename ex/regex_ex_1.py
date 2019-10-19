"""请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

someone@gmail.com
bill.gates@microsoft.com"""
# -*- coding: utf-8 -*-


import re


def is_valid_email(addr):
    re_email = re.compile(r'^[\w]+\.?[\w]+@[\w]+\.com$')
    if not re_email.match(addr):
        return False
    return True


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')