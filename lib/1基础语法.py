import keyword
##########1
print("hello world")

########## 2.变量声明
print("########## 2.变量声明")
r = 20
PI = 3.1415
sArea = r * PI
print (sArea)

# 字符串编码
lan='中文'.encode('utf-8')
print(lan)
print(lan.decode('utf-8'))
value = b'ABC'
print(value)
print('ABC'.encode('ascii'))

# 格式化填充
print('your name: %s age:%d' % ('tiptok',20))
print('input:%s' % (value))
print('input:%s' .format(value))

########## 3.条件
print("########## 3.条件")
if sArea<0:
    print("Yes")
else :
    print("NO")
#缩进不一致会报错  IndentationError: unindent does not match any outer indentation level
print("end")

##########  4.所有关键字
print("##########  4.所有关键字")
print(keyword.kwlist)

##########  5.换行
print("##########  5.换行")
item =["1","2","3"
    ,"4"
]
'''
非[]{}()中的多行语句 ，需要使用
反斜杆（\）进行换行
'''
squart = r +\
+r +\
r
"""
print默认换行 不换行 end=" " 
"""
print("squart:",squart,end=" ")
print(item)



##########  6.字符串
print("\n##########  6.字符串")##加 r R \n不会变成换行
print("string to unicode :",u"string to unicode")##or U


##########  7.输入
# v= input("\n输入Value")
# print("Value：",v)

##########  8.导入 import 与 from...import
'''
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''

