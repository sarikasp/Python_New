info = ['sarika', 'pansare', 24, 51]
print(info)
print(type(info))

# prgram 1
dictInfo =  {
    "firstName":"Sarika",
    "lastName":"Pansare",
    "age":24,
    "rollNo":51
}
print(dictInfo)
print(type(dictInfo))

# prgram 2
# list stores the value by index
flowers = ['orchid', 'lily', 'rose', 'jasmine', 'lotus', 'daisy']
print(flowers)
a1  = len(flowers)
print(a1)


# Dict does not stores value by index
vehicle = {
    #property:value
    #key:value
    "color":"Black",
    "type":"Luxury",
    "color":["White", "Black", "Red"]  # update the color value
}
print(vehicle)


# program 3
animal = {
   "name":"Dog",
    "legs":4,
    "found":["India","USA"]
}
q2 = len(animal)
print(q2)
print(animal)


# program 4

k = [11,22,33]
print(k[1])


MH = {
    "city1":"Pune",
    "city2":"Mumbai"
}
print(MH['city1'])
print(MH['city2'])


# add the property to dict
MH['city3'] = "Nashik"
print(MH)

# update
MH['city2'] = "Ahmednagar"
print(MH)

del MH['city3']
print(MH)


# program 5
bank = {
    "accNo":123,
    "bal":50000000000,
    "branch":"satpur",
    "city":"nashik"
}

# retrive
print(bank["branch"])

# add
bank["pincode"] = 420003
print(bank)

# udpate
bank['accNo'] = 456
print(bank)

# del
del bank['branch']
print(bank)

# program 6
fruits = ["apple","mango","banana","papaya"]

for fr in fruits:
    print(fr)

for fruit in range(len(fruits)):
    print(fruits[fruit])


# ***************************************************


# string booelan int float list
fruit = ["Apple","Mango","Banana","Papaya",]

# add
fruit.append('Guava')
print(fruit)

# update
fruit[2] = 'Tomato'
print(fruit)

# retrive
print(fruit[3])

# remove
fruit.pop(1)
print(fruit)


# dictionary

student2 = {
    "name": "Sarika",
    "lname": "Pansare",
    "age": 24
}

# retrive
print(student2)
print(student2['name'])

# add
student2['isMarried'] = True
print(student2)

# update
student2['name'] = "Gauri"
print(student2)

# remove
del student2['isMarried']
print(student2)


flowers = ['orchid', 'lily', 'rose', 'jasmine', 'lotus', 'daisy']

for fr in flowers:
    print(fr)
# range(n-1)
for fr in range(len(flowers)):
    print(fr)
    print(flowers[fr])


student3 = {
    "name": "Sarika",
    "lname": "Pansare",
    "age": 24,
    'isDrive': True,
    "isMarried": True,
    "city": "Malaysia",
    "skills": ["Python", "Javascript", "Cypress", "Java"]
}

print(student3)

for st in student3:
    # print("******", st) # key
    # print(student3[st]) # value
    print(st, " -- ", student3[st])

#
# # both list updated
a1 = [11,22,33,44,55]
a2 = a1
a1[1] = 222
print(a1)
print(a2)

#
# # both dicttionary updated
vehicle = {
        "Color":"White",
        "City":"Malaysia",
        "RegNo": 456
}

print(vehicle)
vehicle2 = vehicle
vehicle2['Color'] = 'Black'
print(vehicle)
print(vehicle2)
#
#

