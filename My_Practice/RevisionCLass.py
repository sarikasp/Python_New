print("Hello World...!!!")

# Program 1:
x = 100
print(x)
x = 200
print(x)

print("********************************")
# Program 2:

# Arthmetic Operations
# Addition +
# Substraction -
# Multiplication *
# Division /
# Modulus %

a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

print("********************************")
p = 20
q = 10

print(p+q)
print(p-q)
print(p*q)
print(p/q)
print(p%q)


print("********************************")


# DRY -mDon't repeat yourself
# 5 pair -- 25 lines

def Calculator(p,q):
    print(p + q)
    print(p - q)
    print(p * q)
    print(p / q)
    print(p % q)

Calculator(45, 5)
print("********************************")
Calculator(70, 3)
print("********************************")
Calculator(9, 3)
print("********************************")


# Function without parameter and without return type

def addA():
    print(7+8)

addA()
addA()
addA()
addA()
addA()

print("********************************")


# Function with parameter and without return type

def addB(x,y):
    print(x + y)
    print(x * y)
    print(x / y)


addB(4,7)

print("********************************")


# Function with parameter and with return type

def addC(a,b):
    return a+b

x = addC(4,5)
print(x)
print(x + 10)
print(x * 0.10)
print(x - 5)

print("********************************")

def mulA(a,b):
    return a*b

x2 = mulA(3, x)
print(x2)

print("********************************")

a = 10
print(a)
print(type(a))

b = 'Sarika'
print(type(b))

c = True
print((type(c)))

d = 12.4
print((type(d)))

print("********************************")


# Comparison Operator
# <, >, =, >=, <=, ==, !=

print(2>3) # False
print(2<3) # True
print(2<=3) # True
print(2>=3)  # False
print(2!=3) # True
print(2==3) # False
print(3==3) # True


