# Lamba

def add(a,b):
    print(a+b)

add(10,20)


# lamda arguments : expression
# program 1
a1 = lambda a : a +10
print(a1(20))


# program 2
a2 = lambda a, b : a + b
print(a2(20, 30))


# program 3
a3 = lambda a, b, c : a + b + c
print(a3(20, 30, 40))


# program 4
def myFun():
    return lambda a, b : a+b

x = myFun()
print(x(5, 4))


# program 5
y = lambda a, b : a+b
def myFun(n):
    print(n(12, 13))

myFun(y)


# program 6
num = [1,2,3,4,5,6,7,8,9,10]
#[2,4,6,8,10,12,14,16,18,20]
dbl = []

for x in num:
    dbl.append(x*2)

print(dbl)


a2 = list(map(lambda a: a*2, num))
print(a2)


# program 7

listB = [24,5,6,7,8,4,55,66,7]
above10 = []
for x in listB:
    if(x>10):
        above10.append(x)
print(above10)


listC = list(filter(lambda a : a > 10, listB))
print(listC)







