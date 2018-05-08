# 用于正则表达式练习的数据生成器

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime,time

tlds = ('com','edu','net','org','gov')

# randrange 会返回指定递增序列中的一个随机数
for i in range(randrange(5,11)):
    dtint = randrange(time()//1)
    dtstr = ctime(dtint)
    llen = randrange(4,8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen,13)
    dom = ''.join(choice(lc) for k in range(dlen))
    print(
        '%s::%s@%s.%s::%d-%d-%d' %(dtstr,login,dom,choice(tlds),dtint,llen,dlen)
    )