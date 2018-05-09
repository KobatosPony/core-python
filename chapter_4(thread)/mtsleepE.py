# 使用子类化的Thread类

import threading
from time import ctime,sleep

loops = (4,2)

class MyThread(threading.Thread):
    def __init__(self,target,args=(),name=''):
        threading.Thread.__init__(self)
        self.target = target
        self.args = args

    def run(self):
        self.target(*self.args)

def loop(nloop,nsec):
    print('start loop',nloop,'at:',ctime())
    sleep(nsec)
    print('loop',nloop,'done at:',ctime())

def main():
    print('starting at:',ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all done at:',ctime())

if __name__ == '__main__':
    main()