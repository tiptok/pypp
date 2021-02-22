import sys
##迭代器
print('\n## 迭代器')

list =[1,2,3,4]
it = iter(list) #创建迭代器
print(next(it))
print(next(it))

#遍历
for x in it:
    print(x,end=" ")


while True:
    try: ## 冒号不能少 try:  excpet xxx :
        print(next(it))
    except StopIteration:
        print("Iteration Stop")
        break

## 生成器
print('\n## 生成器')
## 斐波那契
def fibonacci(n):
    a,b ,counter =0,1,0
    while True:
        if(counter>n):
            return
        yield a
        a,b = b,a+b
        counter +=1
f = fibonacci(20)

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        print('end')
        break
    
