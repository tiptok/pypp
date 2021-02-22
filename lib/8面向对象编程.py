import types
from enum import Enum,unique
# 类和实例
print("\n8.1 类和实例")
class Man(object):
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
        self.__address ="fujian"  ##私有属性
    def string(self):
        return '%s age is : %s  address:%s'  % (self.Name,self.Age,self.__address)
    def getAddress(self):
        return self.__address
    def walk(self):
        print("man walk to ",self.__address)
    pass

m = Man('tip', 20)
print(m, '/n', Man)
print("new man:", m.Name, m.Age)
print(m.string(),m.getAddress())

# 继承
print("\n8.2 继承")
class OldMan(Man):
    def walk(self):
        print("old man stay in ...")
    pass

oldMan = OldMan("old",90)
print(m.string())
print(oldMan.string())

m.walk()
oldMan.walk()

print("isinstance",isinstance(oldMan,Man))
print("isinstance",isinstance(oldMan,OldMan))
print("isinstance",isinstance(Man,OldMan))


# 获取对象信息
print("\n8.3 获取对象信息")
def fn():
    pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x*x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

print("class dir",dir(oldMan))
print("class hasattr(返回bool值)",hasattr(oldMan,"getAddress"))
print("class getattr(返回属性值)",getattr(oldMan,"Name","default"))
print("class setattr(设置属性值)",setattr(oldMan,"Name","ccc"),oldMan.Name)
# 判断一个类是否有某个方法
if hasattr(oldMan,"getAddress"):
    print("OldMan has method","getAddress")


print("\n8.4 类方法和静态方法")
print("\n1.给实例动态绑定方法")
def printParent(self):
    print("parent is ","ttdd")
Man.printParent = printParent
m.printParent()

print("\n2.类方法/静态方法")
class A(object):
    bar = 'bar'
    @classmethod
    def class_method(self):
        print('class method',self.bar)
    @staticmethod
    def static_method():
        print('static method')
A.class_method()
A.static_method()


## 1.使用__slots__ 限制实例的属性
print("\n8.5 使用__slots__ 限制实例的属性")
class Child(Man):
    __slots__ = ('name','age')
    # def __init__(self,name,age,parent):
    #     self.Name = name
    #     self.Age = age
    #     //self.Father = parent

# child = Child('baby1',1)
# print(child.Father)
# child.Father = 'p2'

# class Baby(object):
#     __slots__ = ('name', 'age')
#
# b1 = Baby()
# b1.name ='cc'
# b1.birth ='2020'

## 2.使用@property
class Student(object):
    def __init__(self, score):
        self._score = score
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('value must be in integer')
        if value<0 or value>100:
            raise ValueError('score must between 0~ 100')
        self._score = value

s1 = Student(100)
s1.score =60 # 101 '101' 会异常
print("property property.setter:",s1.score)

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


## 多3.重继承,定制类
class Animal(object):
    pass

class Runnable(object):
    def run(self):
        print('running ...')


class Flyable(object):
    def fly(self):
        print('Flying ...')

class Dog(Animal,Runnable):
    def __init__(self,name):
        self.nick_name =name
    def __str__(self): #定制方法
        return "class dog:"+self.nick_name
    __repr__ = __str__
d = Dog('duoli')
d.run()
print(d)

# 定义迭代对象
class Fib(object):
    def __init__(self):
        self.a , self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a >100:
            raise StopIteration()
        return self.a
# print(0)
# for n in Fib():
#     print(n)

class FibList(Fib):
    def __getitem__(self, n):
       fib = Fib()
       if isinstance(n,int):
           for i in range (n):
              fib.__next__()
           return fib.a
       if isinstance(n,slice):
            L = []
            start,stop = n.start,n.stop
            if start is None:
                start =0
            for x in range(stop):
                if x>=start:
                    L.append(fib.a)
                fib.__next__()
            return L
print(FibList()[1])
print(FibList()[0:10])


# 4.定制类 动态获取属性
class Chain(object):
    def __init__(self,path=''):
        self.__path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path,path))
    def __str__(self):
        return self.__path
    def __call__(self,path):
        return Chain('%s/%s' % (self.__path, path))
    __repr__ = __str__

# Chain().auth 如果需要继续链式调用 Chain().auth('user')
# 需要定义__call__方法
print(Chain().auth('user').info(1))
print(callable(Chain()))

#5.枚举类

Weekday = Enum('Weekday',('Sun','Mon','Tue','Wed','Thu','Fri','Sat'))
print(Weekday.Mon,str(Weekday.Fri.value))
for name,member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique
class WeekdayClass(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Web = 3
print("Mon",WeekdayClass.Mon,WeekdayClass['Mon'],WeekdayClass(1))
print("Mon value",WeekdayClass.Mon.value)

for name,member in WeekdayClass.__members__.items():
    print(name,"=>",member,member.value)


## TODO:使用元类
'MetaClass Define'

__author__ = 'gitkong'

from enum import Enum, unique


class Filed(object):
    def __init__(self, name, colume_type):
        super().__init__()
        self.__name = name
        self.__colume_type = colume_type

    def log(self):
        print(self)

    def __str__(self):
        return self.__class__.__qualname__


class StringFiled(Filed):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')


class IntegerFiled(Filed):
    def __init__(self, name):
        return super().__init__(name, 'Integer')


class ModelMetaClass(type):
    # attrs {属性名：属性类型,...}
    def __new__(cls, name, bases, attrs):
        # 父类不处理
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        # 声明一个mapper
        mapping = dict()
        for k, v in attrs.items():
            # 判断是不是指定的Filed类
            if isinstance(v, Filed):
                # v.log()
                # 添加参数到mapping中
                mapping[k] = v
        # 移除类属性，防止同名类属性和实例属性冲突
        for k in mapping.keys():
            attrs.pop(k)
        # 绑定一个字典mapper
        attrs['__mapping__'] = mapping
        # 绑定一个表明为类名
        attrs['__table__'] = name
        # print('attrs = ',attrs)
        return type.__new__(cls, name, bases, attrs)


# 定义一个class派生自dict,定义一个方法生成SQL语句
@unique
class SQLType(Enum):
    NoneType = 0
    Create = 1
    Insert = 2
    Delete = 3
    Select = 4


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # 重写setter和getter方法，添加属性自动存储到list中
    def __getattr__(self, key):
        try:
            return self[key]
        except:
            raise AttributeError('Read "Model" Object has no attribute "%s"' % key)

    def __setattr__(self, key, value):
        self[key] = value

    # 生成SQL方法
    def getSQL(self, sqlType=SQLType.NoneType):
        fileds, params, args, typeDict = ([], [], [], [])
        if not isinstance(sqlType, SQLType):
            raise TypeError('Error SQL Type, Please Use SQLType')

        # 读取元类中mapping属性
        for k, v in self.__mapping__.items():
            fileds.append(k)
            params.append('?')
            args.append(getattr(self, k))
            typeDict.append('%s %s' % (v, k))

        if SQLType.Create == sqlType:
            return 'CREATE TABLE %s (%s)' % (self.__table__, ','.join(typeDict))
        elif SQLType.Insert == sqlType:
            return 'INSERT INTO %s (%s) VALUES (%s)' % (self.__table__, ','.join(fileds), ','.join(params))
        elif SQLType.Delete == sqlType:
            return 'DELETE FROM %s' % self.__table__
        elif SQLType.Select == sqlType:
            return 'SELECT %s FROM %s' % (','.join(fileds), self.__table__)
        else:
            return 'ARGS:%s' % str(args)


class User(Model):
    id = IntegerFiled('id')
    name = StringFiled('username')
    email = StringFiled('email')
    # password = StringFiled('password')


user = User(id=12345, name='gitkong', email='xxx.163.com', password='123')
print(user.getSQL(SQLType.Create))
print(user.getSQL(SQLType.Delete))
print(user.getSQL(SQLType.Insert))
print(user.getSQL(SQLType.Select))
print(user.getSQL())

