# Program1:

print("Hello World...!!")
x = 50
print(x)
x = 70
print(x)

# program 2
# Arithmetic operation
# Addition       +
# Subtraction    -
# Multiplication *
# Division       /
# Modulus        %

a = 20
b = 5

print(a + b)
print(a - b)
print(a / b)
print(a * b)
print(a % b)


print(47 % 8)  # 7


print("*****************************************")


q = 10
r = 5

print(q + r)
print(q - r)
print(q * r)
print(q / r)
print(q % r)


print("*****************************************")


# DRY ----- Don't repeat yourself
# 10 pair --- 50 lines
def Calculator(s, p):
    print(s + p)
    print(s - p)
    print(s * p)
    print(s / p)
    print(s % p)


Calculator(32, 4)
Calculator(12, 3)
Calculator(15, 5)


print("*****************************************")


# function without parameter and without return type
def addA():
    print(10 + 5)


addA()
addA()
addA()
addA()
addA()
addA()


print("*****************************************")


# function with parameter and without return type
def addB(a, b):
    print(a + b)


addB(9, 3)
addB(16, 4)
addB(19, 6)


print("*****************************************")


# function with parameter and with return type
def addC(p, q):
    return p + q


q1 = addC(9, 3)
print(q1)
print(q1 + q1)
print(q1 * 0.10)
print(q1 - 2)

print("*****************************************")


def subA(n, m):
    return n - m


q2 = subA(25, 5)
print(q2)
# q2 = 20


def mul(r, t):
    return r * t


q3 = mul(q2, 5)
print(q3)
