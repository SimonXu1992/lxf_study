import time, threading


# 新线程执行的代码
def loop():
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n <= 6:
        n += 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
    print('thread %s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    print("thread %s is running..." % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)