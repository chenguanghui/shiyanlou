import time
from multiprocessing import Process, Value

def func(val):
    for i in range(50):
        time.sleep(0.01)
        val.value += 1

if __name__ == '__main__':
    # 多进程无法使用全局变量，multiprocessing 提供的 Value 是一个代理器，
     # 可以实现在多进程的共享这个变量
    v = Value('i', 0)
    procs = [Process(target=func, args=(v,)) for i in range(10)]

    for p in procs:
        p.start()
    for p in procs:
        p.join()

    print(v.value)