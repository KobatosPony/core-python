# 进程的使用
from multiprocessing import Process,Pool
from concurrent.futures import ProcessPoolExecutor
import time
import random

def work(id):
    print('process %d start...' %id)
    time.sleep(random.randrange(1,3))
    print('%d is End' %id)

if __name__ == '__main__':
    # 使用Process完成多进程
    # p1 = Process(target=work,args=(1,))
    # p2 = Process(target=work,args=(2,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    # 使用Pool(进程池)完成进程
    # 同步
    # pool = Pool(5)
    # for i in range(5):
    #     pool.apply(work,(i,))
    # pool.close()
    # pool.join()

    # 异步
    # pool = Pool(5)
    # for i in range(5):
    #     pool.apply_async(work, (i,))
    # pool.close()
    # pool.join()

    # 使用ProcessPoolExecutor实现
    # 异步
    # pool = ProcessPoolExecutor(5)
    # for i in range(5):
    #     pool.submit(work,i)
    # # shutdown(wait=True)表示会等待所有进程结束然后结束，False则反之
    # pool.shutdown(wait=True)

    # 同步
    pool = ProcessPoolExecutor(5)
    for i in range(5):
        # 使用result会等待进程返回一个结果（可以实现同步）
        res = pool.submit(work,i).result()
        print(res)
    pool.shutdown(wait=True)