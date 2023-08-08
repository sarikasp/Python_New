s = 10
t = 5

print(s+t)
print(s-t)
print(s*t)
print(s/t)
print(s%t)

a = 8
b = 4

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)


# string as a parameter and string as return
def greet(word):
    print("Welcome "+ word)
    return "Welcome "+word
q1  = greet("Sarika")
print(q1)


# boolean as a parameter and boolean as return type

def canDrive(vehicleAvl, age):
    if vehicleAvl and age >= 18:
        print('Drive...!')
        return True
    else:
        print("can't Drive..!!")
        return False

a1 = canDrive(True, 18)
print(a1)


# list as parameter and list as return type

fruits = ["apple","mango","banana"]
def removeFrt(lst):
    lst.remove('banana')
    return lst

a2 = removeFrt(fruits)
print(a2)


# dictionary as parameter and dictionary as return type

info = {
    "firstName":"Sarika",
    "lastName":"Pansare",
    "age":24,
    "rollNo":31
}

def addCity(dict):
    cityAdd = {"city":"pune"}
    dict.update(cityAdd)
    return dict

q4  = addCity(info)
print(q4)


# tuple as a parameter and tuple as return type

numbers = (11,22,33)
def addValue(tupA):
    tupA = list(tupA)
    tupA.append(13)
    tupA = tuple(tupA)
    return tupA

q5 = addValue(numbers)
print(q5)


# set as a parameter and set as return type
setA = {11,22,33}
setB = {33,44,55}

def ComBine(setA,setB):
    return setA.union(setB)
setE = ComBine(setA,setB)
print(setE)

