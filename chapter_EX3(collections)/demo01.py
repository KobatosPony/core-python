# 使用collections中的集合
from collections import *

# 使用namedtuple创建一个自定义的tuple对象
Point = namedtuple("Point",['x','y'])

# 自定义的tuple 包含一个类型名和其中的属性名组成的序列
p1 = Point(1,2)
print(p1.x)

# 可以转化为OrderedDict
print(p1._asdict())

# 可以进行一般元祖的操作
print(str(p1[0])+","+str(p1[1]))

# namedtuple 既有tuple的不变性，还可以根据属性来引用，很方便呢

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# 直接将列表转换为 deque类型
arr_list = ['s','n','o','w']
my_deque = deque(arr_list)

# deque 除了有基本列表的方法外还有哦appendleft 和popleft方法用于从开头添加和去除
my_deque.appendleft('start')
my_deque.append('end')
print(my_deque)

my_deque.popleft()
print(my_deque)

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
# defaultdict 的默认值是调用函数返回的
dd = defaultdict(lambda :None)
print(dd.get('key1'))
dd['key1'] = 'key'
print(dd.get('key1'))

# 除此之外和普通字典的操作一样

# OrderedDict 可以创建一个有序的字典（顺序是插入的顺序）
od = OrderedDict()
od['x'] = 1
od['y'] = 2
od['z'] = 3

# 会按顺序的哦
print(od.keys())

# Counter 是个简单的计数器，可以用来统计字符出现的次数
string = "programing"
ch = Counter()
for s in string:
    ch[s] = ch[s]+1

print(ch)