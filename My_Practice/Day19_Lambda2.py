# program  1

def isEven(x):
    if x % 2 == 0:
        print('Even No')
    else:
        print('Odd No')

isEven(17)
print("----------------")


x1 = lambda a: "Even No" if a % 2 == 0 else "Odd No"
print(x1(40))
print("---------------------------")

def isEven2(x):
    if x % 2 == 0:
        return True
    else:
        return False


listA = [11,22,33,44,55,66,7,33,44,55,66,73]
x2 = list(filter(isEven2, listA))
print(x2)
print("----------------------------")

x3 = list(filter(lambda x : x % 2 == 0,listA))
print(x3)
print("----------------------------")


# program 2  above50

marks = [22,33,44,55,22,33,44,55,66,77]
x4 = list(filter(lambda x : x > 40 ,marks))
print(x4)
print("----------------------------")


# program 3 map()

def sqr(x):
    return x * x

print(sqr(4))
print("-----------------------------------------")

listN = [1,2,3,4,5]
x5 = list(map(sqr,listN))
print(x5)
print("-------------------using lambda function ----------------------")

x6 = list(map(lambda a: a*a,listN))
print(x6)


print("-------- multiplication of 2 lst using lambda function ----------")
# program 4
a = [11,22,33]
b = [44,55,66]

x7 = list(map(lambda a, b: a*b,a, b))
print(x7)


print("-------- birth year using lambda function ----------")

# program 5
birthYear = [1989,1990,1993,1992, 1998, 1996]
x8 = list(map(lambda x : 2023 - x, birthYear))
print(x8)

print("-------- --------- ----------")

from functools import  *
listA = [11,22,33]
sum = 0
for x in listA:
    sum += x

print(sum)


print("-------- using reduce method ----------")
x9 = reduce(lambda x , y: x + y, listA)
print(x9)

print("-------- ------------- ----------")


from functools import reduce

people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 22},
    {'name': 'Charlie', 'age': 28},
    {'name': 'David', 'age': 26},
    {'name': 'Eve', 'age': 19}
]

# Use map to extract ages
ages = list(map(lambda person: person['age'], people))
print("Ages:", ages)
print("-------- ------------- ---------- -------- --------- -------------")

# Use filter to find people above 25
above_25 = list(filter(lambda person: person['age'] > 25, people))
print("People above 25:", above_25)
print("-------- ------------- ---------- -------- --------- -------------")

# Use reduce to calculate total age of people above 25
total_age_above_25 = reduce(lambda acc, person: acc + person['age'], above_25, 0)
print("Total age of people above 25:", total_age_above_25)


print("-------- ------------- ---------- -------- --------- -------------")

people = [
    {
        'name': 'Alice',
        'age': 30 ,
        'city':"pune",
        "skills":["python","java","javascript"]
    },
    {
        'name': 'Bob',
        'age': 22,
        'city':"sangamner",
        "skills":["css3","sql","powerBI"]

    },
    {
        'name': 'Charlie',
        'age': 28,
        'city':"pune",
        "skills":["css3","sql","powerBI"]
    },
    {
        'name': 'David',
        'age': 26,
        'city':"nagpur",
        "skills":["css3","flutter","c#"]
    },
    {
        'name': 'Eve',
        'age': 19,
        'city':"jaipur",
        "skills":["css3","flutter","c#"]
    }
]

# program 1

# all cities
#people = [dic1,dic2,dic3,dic4,dict5]

listA = [11,22,33,44,55,66]
# [12,23,34,45,56,67]
print(list(map(lambda x: x+1, listA)))
print("-------- ------------- ---------- -------- --------- -------------")

# print city to every people
print(list(map(lambda person: person.get('city'), people)))
print("-------- ------------- ---------- -------- --------- -------------")

# program 2
# add  git as skill to every people

print(list(map(lambda person: person['skills'].append('git'), people)))
print(people)
print("-------- ------------- ---------- -------- --------- ------------- ---------- -------- --------- -------------")

for x in people:
    x['skills'].append('Salesforce')
print(people)

print("-------- ------------- ---------- -------- --------- ------------- ---------- -------- --------- -------------")

# people belong to pune city
# program3
a1 = list(filter(lambda person: person['city'] == 'pune', people))
print(a1)

print("-------- ------------- ---------- -------- --------- ------------- ---------- -------- --------- -------------")
for a in a1:
    print(a['name'])
print("-------- ------------- ---------- -------- --------- ------------- ---------- -------- --------- -------------")

# program 4
# alice:3

a2 = list(map(lambda person: person['name']+ ":" + str(len(person['skills'])), people))
print(a2)
print("-------- ------------- ---------- -------- --------- ------------- ---------- -------- --------- -------------")

# program 5

j = [11,22,33]
print(reduce(lambda acc, y: acc+y, j,5))

print("-------- ------------- ---------- -------- --------- ------------- ---------- -------- --------- -------------")

print(reduce(lambda acc, person: acc + person['age'], people, 0) / len(people))



