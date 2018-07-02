def testFun():
    # temp = [lambda x : i*x for i in range(4)]
    temp = []
    for i in range(4):
        def show(x):
            return i*x
        temp.append(show)

    return temp

for everyLambda in testFun():
    print (everyLambda(2))

# 在这里因为闭包的原因会打印6,6,6,6而不是0,2,4,6