from functools import reduce

# map reduce
def f(x):
    return x*x

print(list(map(f,[1,2,3,4,5])))
print(str(1))
print(list(map(str,[1,2,3,4,5]))) # 将list所有数字转为字符串


def fn(x,y): # reduce reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
    return x*10 + y
print(reduce(fn,[1,2,3,4,5]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))
print("str2int:",str2int("456789123"))

def char2num(s):
    return DIGITS[s]

def lambda_str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))
print("str2int:",lambda_str2int("456789123"))

def normalize(name):
    return str(name[0]).upper() + str(name[1:]).lower()
print(list(map(normalize,['adam', 'LISA', 'barT'])))

def prod(L):
    def agg(x,y):
        return x*y
    return reduce(agg,iter(L))

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def str2float(s):  # str转为 浮点数
      L = s.split('.')
      L = map(int,L)
      def trans(x,y):
          i = len(str(y))
          return x +y/pow(10,i)

      return reduce(trans,L)
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


# filter
def is_odd(n):
    return n%2 == 1

print("is_odd:",list(filter(is_odd,[1,2,3,4,5])))

def not_empty(s):
    #return s and s.strip() #len(s.strip())>0
    #return  (not s is None) and len(s.strip())>0
    return  s and len(s.strip())>0

print("str_not_empty:",list(filter(not_empty,['A', '', 'B', None, 'C', '  '])))

def is_palindrome(n): #判断回文
    num = str(n)
    if (num==num[::-1]):
        return int(num)
    else :
        return False
print("is_palindrome:",list(filter(is_palindrome,range(100))))


# sorted
sortNumList = [36, 5, -12, 9, -21]
print("sorted :", sorted(sortNumList))
print("sorted key=abs:", sorted(sortNumList, key=abs))

sortStrList = ['bob', 'about', 'Zoo', 'Credit']
print("sorted key=str.lower",sorted(sortStrList,key=str.lower))

LSet = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return  t[0]
def by_score_desc(t):
    return  -t[1]
L2 = sorted(LSet, key=by_name)
print("sorted by name:",L2)
print("sorted by name:",sorted(LSet,key=by_score_desc))



## 返回函数
def lazy_sum(*args):
    def sum():
        total = 0
        for n in args:
            total = total + n
        return total
    return sum

f = lazy_sum(*[1,2,3,4,5])
print("lazy_sum:",f())

## 匿名函数
def f(x):
    return x * x
print(list(map(f,range(10))))
print(list(map(lambda x:x*x,range(10))))

## 高阶函数
def func(g,arr):
    return [g(x) for x in arr]

def double(x):
    return 2*x
def square(x):
    return x*x
print("\n--高阶函数--")
print("double:",func(double,[1,2,3,4,5]))
print("square:",func(square,[1,2,3,4,5]))

## map/reduce/filter
print("\n--map/reduce/filter--")
m1 = list(map(double,[1,2,3,4,5]))
print("map double:",m1)
print("reducce square:",reduce(lambda x,y:x*y,[1,2,3,4,5])) # 相当于 ((1 * 2) * 3) * 4
print("filter even_num",list(filter(lambda x:x%2==0,[1,2,3,4,5]))) ## x%2==0 返回偶数部分  x%2 返回奇数部分

## 带状态的闭包函数
print("\n 带状态的闭包函数")
from math import sqrt
def point(x,y):
    def get_distance(u,v):
        return sqrt((x - u) ** 2 + (y - v) ** 2)
    return get_distance

pt = point(1,1)
print(pt(10,10))


## partial 函数
print("\n partial 函数")
from functools import partial

def multiply(x,y):
    return x * y

#把一个函数的某些参数给固定住，返回一个新的函数
double_mul = partial(multiply,y=2)
print(double_mul(10))