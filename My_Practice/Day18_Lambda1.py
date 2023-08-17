# square of a numbers

# program 1
a = lambda a: a * a
print(a(4))
print("----------------")


# addition of two numbers
# program 2
a2 = lambda a, b : a + b
print(a2(4, 6))
print("----------------")


# greatest of two element
# program 3
a3 = lambda a, b : a if a > b else b
print(a3(8, 9))
print("----------------")


# program 4 - as a return type

def addA():
    return lambda a, b : a+b

a4 = addA()
print(a4(34, 54))
print("----------------")



# program 5   -- as a parameter

a5 = lambda x,y : x * y
print(a5(9,8))
print("----------------")

def mulB(fn):
    print(fn(4,5))

mulB(a5)
