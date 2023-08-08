# Types

# Introvert / Extrovert
# less social   more social
# less outing   more social
# calm          loud

# Human
# Properties - color , height ,weight ,gender
# Methods - talk() , walk()

# Vehicle
# Properties - color , type , model , name ,regNo
# Methods - start() , stop()

# Bank
# Properties - bal , accNo ,accType , accName , branch
# Methods - Deposit() , Withdrawl()


a = 4
print(a)
print(type(a))  # <class 'int'>


b = 9.8
print(b)
print(type(b))  # <class 'float'>


c = True
print(c)
print(type(c))  # <class 'bool'>


cc = False
print(cc)
print(type(cc))  # <class 'bool'>


d = "Sarika"
print(d)
print(type(d))  # <class 'str'>


# comparison
# entity < entity -----> boolean --- type
# < , > ,<=, >= ,!= ,==

print(2 >3)  # False
print(2 < 3) # True
print(2 <=3) # True
print(3 >= 2) # True
print(2 != 3) # True
print(2 == 3) # False
print(3 == 3) # True


# Logical Operators

# AND

# True  and  True  ==== True
# False  and  True  ==== False
# True   and  False ==== False
# False  and  False ==== False

print( 3 == 3 and 7 != 6)  # True
print( 3 != 3 and 7 != 6) # False
print( 3 == 3 and 7 == 6)  # False
print( 3 != 3 and 7 == 6)  # False

# OR

# True  or  True  ====> True
# False  or  True  ====> True
# True   or  False ====> True
# False  or  False ====> False

print( 3 == 3 or 7 != 6)  # True
print( 3 != 3 or 7 != 6)  # True
print( 3 == 3 or 7 == 6)  # True
print( 3 != 3 or 7 == 6)  # False


# NOT
print(not (7==7))  # False
print(not (7!=7))  # True

