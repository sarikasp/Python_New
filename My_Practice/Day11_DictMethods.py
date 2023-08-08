# program 1
stud = {
        'fname': "Sarika",
        "lname": "Pansare",
        "age": 24,
        'city': "Malaysia"
}

print(stud)
print(type(stud))
stud2 = stud
stud2['fname'] = "Gauri"
print(stud)
print(stud2)
print("*****************************************************************************")

# program 2

age = 24
stud = {
        'fname': "Sarika",
        "lname": "Pansare",
        "age": age,
        'city': "Malaysia"
}

# existing list is not updated, new list is updated
stud2 = stud.copy()
stud2['fname'] = "Gauri"
print(stud)
print(stud2)

stud2['age'] = 25
print(stud2)
print("*****************************************************************************")


# program 3
a = 987
vehicle = {
        "color":"red",
        "type":"sedane",
        "regno":a
}

# pop() - removes
vehicle.pop('color')
print(vehicle)


# program 4
# get()
a1 = vehicle.get('type')
print(a1)
a5 = vehicle.get('Type')
print(a5)
# print(vehicle['Type'])
print("*****************************************************************************")


# program 5

stud = {
        'fname': "Sarika",
        "lname": "Pansare",
        "age": 24,
        'city': "Malaysia"
}

for st in stud:
        print(st, stud[st])

print("*****************************************************************************")

# keys()
for st in stud.keys():
        print(st)
print("*****************************************************************************")

# values()
for st in stud.values():
        print(st)
print("*****************************************************************************")

# items() - return tuple
for st in stud.items():
        print(st)
print("*****************************************************************************")

# clear()
stud2.clear()
print(stud2)
print("*****************************************************************************")

# fromkeys()
keys = ('name', 'lname', 'age')
val = None
a2 = dict.fromkeys(keys, val)
print(a2)
print("*****************************************************************************")

# update()
a2.update({'name': 'Sarika', 'rollNo': '32'})
print(a2)
print("*****************************************************************************")


stud = {
        'fname': "Sarika",
        "lname": "Pansare",
        "language": 'Marathi',
        "age": 24
}

# popitem()
stud.popitem()
print(stud)
print("*****************************************************************************")
DY
# setdefault()
a3 = stud.setdefault('city', 'Malaysia')
print(a3) # Malaysia
a4 = stud.setdefault('language', None)
print(a4)
print(stud)
a6 = stud.setdefault('RollNo', 31)
print(a6)
