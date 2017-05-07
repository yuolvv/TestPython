list = [36,5,-12,9,-21]
liststr = ["bob","about","Zoo","Credit"]

a = sorted(list)
print(a)

b = sorted(list,key=abs)
print(b)

c = sorted(liststr)
print(c)

d = sorted(liststr,key=str.lower)
print(d)

e = sorted(liststr,key=str.lower,reverse=True)
print(e)