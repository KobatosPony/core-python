# 运算符重载

class List:
    def __init__(self,data):
        self.data = data

    def __del__(self):
        print(self.data)

    # 使用 __slots__ 对类中的属性进行限制（参数为元祖）
    __slots__ = ('data')

    # 如果在类中定义的话，则对于实例的索引运算，会自动调用__getitem__。
    # 当实例X出现X[i]这样的索引运算时，Python会自动调用__getitem__方法
    def __getitem__(self, item):
        print("get index: ",item)
        return self.data[item]

    def __setitem__(self, key, value):
        print("set index: ",key,"to",value)
        self.data[key] = value

    def __call__(self, *args, **kwargs):
        print("实例调用时使用！")
        

class Number:
    # __init__事实上也是运算符重载
    def __init__(self,data):
        self.data = data

    def __del__(self):
        print("Value: "+str(self.data))

    # __str__ 和 __repr__ 返回一个字符串
    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

    def __add__(self, other):
        return self.data + other

    def __radd__(self, other):
        return self.data + other

if __name__ == '__main__':
    arr = List([1,2,3,4,5,6,7])
    print(arr[2])
    arr[1] = 10

    # 迭代时会使用__getitem__方法（会优先考虑__iter__）
    for item in arr:
        print(item)

    arr()

    num_1 = Number(100)
    print(num_1)

    num_2 = Number(100)
    num_sum = num_1 + num_2
    print(num_sum)

