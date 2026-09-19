n = 314
# lis = list(n)
# print(lis)
print(type(n))
lis = [int(d) for d in str(n)]
print(lis)

x = 3.0
print(type(x))
print(x.is_integer())
li = [int(c) for c in str(x).replace('.','')]
print(li)

name = "Aliae"
print(name.upper())
print(name.lower())
print(name.replace("A", "B"))

def myih():
    print('hello')

print(type(myih))
myih()

class mi:
    pass

print(type(mi))
