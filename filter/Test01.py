print("\\\n\\")
print(3>2)
print(True or False)

age = 2
if age >=18:
    print("成年人")
else:
    print("未成年人")

a='aaaa'
print(a)

#/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
print(9/3)    #3.0
print(10/3)   #3.3333333333333335
#//称为地板除，两个整数的除法仍然是整数
print(10//3)  #3

print("包含中文的string")

#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(chr(66))

print('\u4e2d\u6587')

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len('ABC'))
print(len('中文'))

print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

print('Hello,%s' %'ting')
print('%.2f'%3.14159265359)