print("这是返回函数的demo")

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3= count()
print(f1())
print(f2())
print(f3())


print("这是匿名函数的demo")

#lambda表达式
a = list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9]))
print(a)

b = lambda x:x*x
print(b(5))

print("这是装饰器的demo")

def now():
    print('2016-6-3')
c=now
c()

print(now.__name__)
print(c.__name__)

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now1():
    print("200000000")
now1()

print("这是偏函数的demo")

d = int('12345')
print(d)

d1 = int('12345',base=8)
print(d1)

d2 = int('12345',base=16)
print(d2)

d3 = int('101010',base=2)
print(d3)

def int2(x,base=2):
    return int(x,base)
e1 = int2('1000000')
print(e1)
e2 = int2('1010101')
print(e2)







