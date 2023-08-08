# name = 'sarika'
# a1 = 'q' in name
# print(a1)
#
#
# flowers = ['orchid', 'jasmine', 'lily', 'lotus', 'rose']
# print(flowers)
#
# for fr in flowers:
#     print(fr)
#
# # for fr in 5
# for fr in range(len(flowers)):
#     print(flowers[fr])
#
# # for x in range(10):
# #     print(x)
#

# student = {
#     "name": ["Sarika", "Gauri", "Snehal", "Shubhangi"],
#     "lname": "Pansare",
#     "age": 24
# }
#
# # retrive
# print(student)
# print(student['lname'])
#
# # add
# student['city'] = 'Malaysia'
# print(student)
#
# # update
# student['city'] = 'Pune'
# print(student)
#
# # delete
# del student['city']
# print(student)


# names =student['name']

# print(names[1])
# names =student['name'][1]
# print(names)

# for name in names:
#     print(name)


# upper()
name = "sarika"
print(name.upper())

# lower()
name2 = "GAURI"
print(name2.lower())

# count()
name3 = "SarikaSnehal"
print(name3.count('S'))


# startswith()
print(name3.startswith('Sar'))

# endswith()
print(name3.endswith('hagl'))

# len()
print(len(name3))


# split()
a1 = name3.split('a')
print(a1)


# replace()
lang = 'I am learning Javascript'
print(lang)
a2 = lang.replace('Javascript', 'Python')
print(a2)

# isdigit()
num = "1234"
a3 = num.isdigit()
print(a3)


# isalpha()
name4= ' sarika'
a4 = name4.isalpha()
print(a4)

# isalnum()
name5= '1sa2ri4ka'
a5 = name5.isalnum()
print(a5)


# capitalize()
name6 = 'sarika shankar pansare'
a6 = name6.capitalize()
print(a6)

a7 = 'i am learning javascript'
a8 = a7.capitalize()
print(a8)

# title()
a9 = name6.title()
print(a9)
a10 = a7.title()
print(a10)


# strip()
name7 = "  sarika  "
print(len(name7))
a11= name7.strip()
print(a11)
print(len(a11))

# lstrip()
name7 = "  sarika  "
a11= name7.lstrip()
print(a11)
print(len(a11))


# rstrip()
name7 = "sarika  "
a11= name7.rstrip()
print(a11)
print(len(a11))

# swapcase()
city = "MalaYsIa"
a12= city.swapcase()
print(a12)


# index()
print(city.index('a'))
