# 使用threading模块

import threading
from time import sleep,ctime

loops = [4,2]

def loop(nloop,nsec):
    print('start loop',nloop,'at:',ctime())
    sleep(nsec)
    print('loop',nloop,'done at:',ctime())

def main():
    print('starting ay:',ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)

    for j in nloops:
        threads[j].start()

    for k in nloops:
        threads[k].join()

    print('all done at:',ctime())

if __name__ == '__main__':
    main()