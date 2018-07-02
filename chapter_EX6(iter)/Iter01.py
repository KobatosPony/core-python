import itertools
from collections import Iterable,Iterator

seq = [i*2 for i in range(10)]

# 迭代器是一次性的，如果没有next就相当于空
seq_iter = iter(seq)
print(6 in seq_iter)
print(6 in seq_iter)

# 可迭代类型不等于迭代器
print(isinstance(seq,Iterable))
print(isinstance(seq,Iterator))