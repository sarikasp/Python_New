
#program 16

city7 = " goa "
# print(len(city7))
# q1 = city7.strip()
# print(len(q1))

# program 17
city8 = " Bhopal"
q2 = city8.lstrip()
print(len(q2))

# program 18
city9 = " wardha "
print(len(city9))
q3 = city9.rstrip()
print(len(q3))

# program 19
info = "I am  learning js "
q4 = info.title()
print(q4)

# program 20
city10 = "indore is nice place to leave"
q5 = city10.capitalize()
print(q5)

# program 21
city11 = "NaGpur"
q6 = city11.swapcase()
print(q6)

# program 22

city13 = "jaipur"

# 0     1    2    3    4   5
# j     a    i    p    u   r
q7 = city13.index("a")
print(q7)

# 0  1  2  3  4  5  6  7  8  9 10 11 12
# c  h  a  n  d  r  a  p  u  r  a  e  a

city14 = "chandrapuraea"
q8 = city14.index("a",5)
print(q8)

q9 = city14.index("a",7,11)
print(q9)

first_name = "chinmay"
lastName = "deshpande"
print("My firstname is {} and lastName is {}".format(first_name,lastName))


# ----------------------------------------------------------------
# 'in' keyword

fruits = "apple mango banana chikoo papaya"
if "apple" in fruits:
    print("fruit is available")
else:
    print("fruit is not available")


print("c" in "chinmay")
