from io import StringIO,BytesIO
import  os
import  json
# 1.文件读写
f = open('hello.py','r',encoding='UTF-8')
print(f.readline())

def load_file(path):
    try:
        f = open(path,'r',encoding='UTF-8')
        print(f.readline())
    finally:
        if f:
            f.close()
    return
load_file('hello.py')

def read_lines(path):
    with open(path,'r',encoding='UTF-8') as f:
        for line in f.readlines():
            print(line.strip())

# read_lines('hello.py')

def write_file(path):
    with open('abc.text','w') as f:
        f.writelines('Hello.world')

# 2.StringIO 和 BytesIO
f = StringIO()
f.write('hello')
f.write(' tiptok')
print(f.getvalue())

bf = BytesIO()
bf.write('中文'.encode('utf-8'))
print(bf.getvalue())

print('os.name %s name:%s' % (os.name,''))
print(os.environ)
print('查看环境变量：',os.environ.get('GO111MODULE'))
print('查看文件目录',os.path.abspath('.'),os.path.join('\\a\\b','c'))

# 4.序列化
mUser = dict(name='tiptok',age=10,score=20)
marshStr = json.dumps(mUser)
print(marshStr)
def dict2student(d):
    return (d['name'], d['age'], d['score'])
unMarshObj = json.loads(marshStr) #,object_hook=dict2student
print(unMarshObj,unMarshObj['name'],unMarshObj['age'])