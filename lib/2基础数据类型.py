####### 1.多变量赋值
a,b,c =1,2,"run"
print(a,b,c)


####### 2.标准数据类型
#Number 数字
#int(只有一个int表示长整形)  float bool complex
print("#Number 数字")
a,b,c,d = 20,5.5,True,4+3j
print(type(a),type(b),type(c),type(d))
#还可以用 isinstance 来判断类型
print("instance",isinstance(a,int))


#Number string
print("\nstring 字符串")
word ="Python"
#字符串有两种索引方式，从左往右以0开始，从右往左以-1开始
print(word[0],word[5])
print(word[-6],word[-1])

#List 列表
print("\n#List 列表")
listObject =['abc', 789, 2.33, 'ccc', 'dddd']
tinglist =[156,'of']

##list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
 
print (listObject, len(listObject), listObject[0], listObject[-1])            # 输出完整列表  0:输出列表第一个元素  -1：输出列表最后一个元素 -2/-3 倒三倒四
print (listObject[0])         # 输出列表第一个元素
print (listObject[1:3])       # 从第二个开始输出到第三个元素
print (listObject[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (listObject + tinylist) # 连接列表

print("列表插入/移除")
listObject.insert(0, "cccddd")
print(listObject)
listObject.pop()
listObject.append("append")
print(listObject)

#Tuple（元组）
print("\n#Tuple（元组）")
tuple = ('c11','dhl','hh')
#不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开
tup1 = ()    # 空元组
tup2 = (20,) # 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义



#Set（集合）
print("\n#Set（集合）")
'''
集合（set）是一个无序不重复元素的序列。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
#paset ={v1,v2}
#paset2 = set(value)
'''

stu ={'ccc','tip','tok','tip'}
print(stu)##自动过滤重复的项

if('cz' in stu):
    print('cz in stu')
else:
    print('cz not in stu')

a = set('abcdefg')
b = set('efgh')
print(a)

print(a - b)     # a和b的差集
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素


#Dictionary（字典）
print("\n#Dictionary（字典）")
dic ={}
dic['1'] = 1
dic['2'] = 2

tinydic = {'name':'ccc','age':12}
print(dic['1'])
print(tinydic)
print(tinydic.keys())
print(tinydic.values())

###实例 dictionary
print('\n##实例 dictionary')
dict([('runoob',1),('geogle',2)])
dict(runoob=1,geogle=2)

print(int('32',10)) #32
print(int('32',16)) #50

print(hex(20)) #0x14

##函数返回多个值
print('\n##函数返回多个值')
def example(a,b):
    return (a,b)
print(example(5,6))

##函数不定长度参数
print('\n##函数不定长度参数')
def test(*args):
    print(args)
    return args

print(type(test(5,8,2,0)))


##输出字典扩展
print('\n##输出字典扩展')
def pDic(d):
    for c in d:
        #print(c)
        print(c,':',d[c])
    # items()函数
    for k,v in d.items():
        print(k,':',v)

pDic(dic)


##类型判断扩展
print('\n##类型判断扩展')
'''
type 是用于求一个未知数据类型对象，而 isinstance 是用于判断一个对象是否是已知类型。
type 不认为子类是父类的一种类型，而isinstance会认为子类是父类的一种类型。
可以用 isinstance 判断子类对象是否继承于父类，type 不行。
综合以上几点，type 与 isinstance 虽然都与数据类型相关，但两者其实用法不同，
type 主要用于判断未知数据类型，isinstance 主要用于判断 A 类是否继承于 B 类
'''
class father(object):
    pass
class son(father):
    pass
print(type(son()),type(son())==father)
print(isinstance(son(),father))
print(type(son()))
print(type(son))


# 然后修改脚本权限，使其有执行权限
# chmod +x hello.py

# 条件判断
height = 1.75
weight =75
bmi = weight/(height**2)
if bmi<18.5:
    print('过轻')
elif bmi<25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')

# 循环
names =['tip','tok','hello','python']
for name in names:
    print(name)
print("sort list",names.sort(),names) #列表排序
sum = 0
for x in [1,2,3,4,5]:
    sum = sum+x
print(sum)
sum = 0
for x in range (10):
    sum = sum + x
print(sum)

print("range",range(5))
listRange=list(range(5))
print("list range:",listRange)

sum = 0
n = 10
while n>0:
    if n==2:
        break  #continue
    sum = sum +n
    n = n-2
print("while",sum)

# dict 字典
dictUserScore = {"tip":80,"tok":60,"ccc":50}
print("map['tip']=",dictUserScore["tip"])

print('dict exits key (ho)', 'ho' in dictUserScore,'tip' in dictUserScore)

print(dictUserScore.get('ho'),dictUserScore.get('ho',99)) #  通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
#dictUserScore.pop('ho') #删除键值
dictUserScore.pop('tip')

# set
set1 = set([1,2,3,2,3])
print("set1",set1)
set2 = set([1,2,4])
print("set &",set1 & set2)
print("set |",set1 | set2)