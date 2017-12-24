from multiprocessing import Pool

def f(i):
    print(i, end=' ')

def main():
      # 初始化一个 3 个进程的进程池
    pool = Pool(processes=3)
    for i in range(30):
           # 调用 apply 方法开始处理任务，传入任务处理函数 f，和参数 i
        pool.apply(f, (i,))

if __name__ == '__main__':
    main()