"""
下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
"""
import subprocess

if __name__ == '__main__':
    print("$ nslookup www.python.org")
    r = subprocess.call(['nslookup', 'www.python.org'])
    print("Exit code:", r)
