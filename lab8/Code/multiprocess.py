import os
from multiprocessing import Process

def hello(name):
    print('child process: {}'.format(os.getpid()))
    print('Hello ' + name)

def main():
     # 注意：args 参数要以 tuple 方式传入
    p = Process(target=hello, args=('shiyanlou', ))
    p.start()
    p.join()
    print('parent process: {}'.format(os.getpid()))

if __name__ == '__main__':
    main()