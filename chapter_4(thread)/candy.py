# 使用型号量和锁来实现糖果机

from atexit import register
from random import randrange
# BoundedSemaphore 为信号量
from threading import BoundedSemaphore,Lock,Thread,RLock
from time import sleep,ctime

# 初始化设置
lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print('Refilling candy')
    try:
        # 信号量+1，如果满了则抛出ValueError
        candytray.release()
    except ValueError:
        print('Full skipping')
    else:
        print('OK')
    lock.release()

def buy():
    lock.acquire()
    print('Buying candy...')
    # 信号量-1，如果满了则抛出ValueError
    if candytray.acquire(False):
        print('OK')
    else:
        print('Empty , skipping')
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

def _main():
    print('starting at:',ctime())
    nloops = randrange(2,6)
    print('The candy machine (full with %d bars)' %MAX)
    # 购买糖果的线程
    Thread(target=consumer,args=(randrange(
        nloops,nloops+MAX+2),)).start()

    # 生产糖果的线程
    Thread(target=producer,args=(nloops,)).start()

@register
def _atexit():
    print('all done at:',ctime())

if __name__ == '__main__':
    _main()