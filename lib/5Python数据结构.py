from collections import deque
#列表 是 可变的
a =  [66,77,88,88,99]
print(a.count(88),a.count(99))
a.insert(1,55)
print(a)

print(a.index(66))
a.remove(88)#移除列表里面的第一个匹配项
print(a)

a.reverse()
print(a)

a.sort()
print(a)


#列表当做堆栈使用
print("\n ##列表当做堆栈使用")
stack =[3,4,5]
stack.append(6)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

#从列表最后一个读取速度快 从列表头读取慢
queue = deque(["ddd","ccc","fff","eee"])
queue.append("kk")
print(queue)

queue.popleft()#从左边读取
print(queue)


#列表推导式
print("\n## 列表推导式")
vec =[2,4,6]
print([3*x for x in vec])

#模块
print("\n## 模块")

if __name__ =='__main__':
    print('main')
else:
    print("来自其他模块")

#内置的函数 dir() 可以找到模块内定义的所有名称
print(dir(deque))

#包
#目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包

# 切片
n = 3
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
topL = []
for i in range(n):
    topL.append(L[i])
print(topL,"\n",L[0:3])

print("list enumerate:")
for i,value in enumerate(L):
    print(i,value)

# map
print("map items:")
m = {"A":"1","B":"b","C":'c'}
for key,value in m.items():
    print(key,value)

# 查询列表最大值 最小值
def findMinAndMax(L):
    if len(L)==0:
        return (None,None)
    min = max = L[0]
    for x in L:
        if x<min:
            min = x
        if x>max:
            max = x
    return (min,max)


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

# 列表生成式
print("列表生成式")
print([x*x for x in range(1,11)]) # 1*1 ... 10*10
print([x*x for x in range(1,11) if x % 2 ==0]) #筛选除偶数
print([m + n for m in 'tip' for n in 'tok'])#两层循环
print([k+'='+v for k,v in m.items()])
print([s.lower() for s in L])


# 生成器
print("生成器")
genNumber = (x*2 for x in range (0,11))
for x in genNumber:
    if x == 20:
        print(x)


def fib(max):
    n, a, b = 0, 0, 1
    while n<max:
        yield b
        a , b = b , b + a
        n = n + 1
    return 'done'
print('fib:',fib(10))

fibL = []
for x in fib(10):
    fibL.append(x)
print('fib list:',fibL)

gfib = fib(10)
print("fib generator next:",next(gfib),next(gfib)) # 多次调用next 超过10以后 出现错误 StopIteration

while True:
    try:
        x = next(gfib)
        print('fib generator next:',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

print('杨辉三角')
def triangles():
    tl = []
    while True:
       l = [v if i == 0 else tl[i] + tl[i - 1] for i, v in enumerate(tl)]
       l.append(1)
       tl = l
       yield tl
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')


# 迭代器
it = iter([1,2,3,4,5])
while True:
    try :
        x = next(it)
    except StopIteration as e:
        print(e.value)
        break
        
##凡是可作用于for循环的对象都是Iterable类型；
##凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
##集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
##Python的for循环本质上就是通过不断调用next()函数实现的
for x in [1,2,3,4,5]:
    pass