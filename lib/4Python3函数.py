##函数
print('\n## 函数')
'''
def 函数名（参数列表）:
    函数体
'''
def Hello():
    print("hello,world")

Hello()

def Area(width,height=10):
    #指定height的默认值为 10  默认参数不放最后会报错
    return width * height

print(Area(5,6))


##函数调用
print('\n## 函数调用')

## 可更改(mutable)与不可更改(immutable)对象
#strings tuples numbers 是不可更改对象
#list dict 等则是可以修改的对象
'''
不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，
再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，
本身la没有动，只是其内部的一部分值被修改了
'''

def ChangeInt(a):
    a = 10

b = 2
ChangeInt(5)
print(b) #结果还是 2


##不定长 参数
print('\n## 不定长 参数')
def printInfo(*vartuple):
    for var in vartuple:
        print(var)
    return;

printInfo(7.0,50,88,66)


##匿名函数
print('\n##匿名函数')
## lambda [arg1 [,arg2,.....argn]]:expression

sum = lambda s1,s2:  s1+s2;
print(sum(10,30))
print(sum(2.2,30))

##作用域
'''
x = int(2.9)  # 内建作用域
 
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
'''

# 1.函数调用
print('abs:',abs(-100))
print('max:',max(-100,100,50))
print(int('123'),int(12.34),float(12.34))
print(str(123),bool(1),bool(''))
print('hex str',str(hex(2555)))

# 2.定义函数
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
print('abs:',my_abs(-100))
#print(my_abs('A'))

# 2.1 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return
def return_none():
    return
print('return:',return_none())

# 2.2  定义可变参数 参数numbers接收到的是一个tuple
# *args 是可变参数，args接收的是一个tuple
def calc(*number):
    sum = 0
    for n in number:
        sum = sum + n*n
    return sum

print(calc(1),calc(2,2))
# list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = (10,5,2)
print(calc(*nums))

# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# **kw接收的是一个dict
def person(name, age, **kw):
    if 'city' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('ttt', 30)
person('ttt', 30, country='fj', gender='F')

extral ={'city':"beijin",'job':"solf"}
person('ttt', 30,**extral)
person('ttt', 30,**{'city':"beijin",'job':"solf"})


# 命名的关键字参数   为了限制调用者可以传入的参数名，同时可以提供默认值
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数

def person(name, age,*, city='bj', job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing',job= 'Engineer')
person('Jack', 24, job= 'Engineer')

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))

def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
print(fact_iter(5,1))

def trim(s):
    while s != '' and s[0] == ' ':
        s = s[1:]
    while s != '' and s[-1] == ' ':
        s = s[:-1]
    return s

if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功7!')