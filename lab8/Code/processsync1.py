import time
from multiprocessing import Process, Value, Lock

def func(val, lock):
    for i in range(50):
        time.sleep(0.01)
        # with lock 语句是对下面语句的简写：
        #
        # lock.acquire()
        # val.value += 1
        # lock.release()
        #
        with lock:
            val.value += 1

if __name__ == '__main__':

    v = Value('i', 0)
    ＃ 初始化锁
    lock = Lock()
    procs = [Process(target=func, args=(v, lock)) for i in range(10)]

    for p in procs:
        p.start()
    for p in procs:
        p.join()

    print(v.value)