# Program 1
fruits = ['apple', 'mango', 'banana', 'grapes']
print(fruits[0])
print(fruits)
print(type(fruits))

fruitsA = ('apple', 'mango', 'banana')
print(fruitsA)
print(fruitsA[2])
print(type(fruitsA))
# fruitsA = fruitsA[3] = 'grapes'
# print(fruitsA)


# tuples store the value by index
# tuples does not support item assignment
# tuple is fixed length
# tuple can store duplicate values


vegetables = ('brinjal', 'carrot', 'cauliflower', 'cabbage', 'carrot')
print(vegetables[0])
print(vegetables[2])
print(vegetables)

# vegetables[4] = 'ladyfingure'
# print(vegetables)

cabDrive = (True, False, False, True)
numberTuple = (11,22,3,44,55)
listTuple = ([11,22], ['sarika', 'chinmay'], [True, False])
dictTuple = (
    {"firstName": 'chinmay', 'lastName': 'deshpande'},
    {"firstName": 'sarika', 'lastName': 'pansare'}
)


# Program 2

#             0          1          2           3          4       5
country = ('india', 'pakistan', 'malaysia', 'canada', 'srilanka', 'uk')
#            -6         -5           -4          -3         -2     -1

print(country[1])
print(country[-1])

# tuple[startIndex: endIndex(optional)]
print(country[1:])
print(country[1:4])
print(country[-4:4])
print(country[4:])
print(country[0:-1])


print('india' in country)
print('Malaysia' not in country)

if('india' in country):
    print('coutry exist')
else:
    print('country not exist')


# update

flowers = ('orchid', 'lily', 'rose', 'jasmine', 'lotus', 'daisy', 'orchid')
# error
# flowers[1] = 'jasmine'
# print(flowers)
print(type(flowers))
print(flowers)
flowers = list(flowers)
print(type(flowers))
print(flowers)

flowers[1] = 'jasmine'
print(flowers)
flowers = tuple(flowers)
print(flowers)
print(type(flowers))


tupleA = (11,22)
tupleB = (33,44)
tupleC = tupleA + tupleB
print(tupleC)


tupleD = tupleA * 4
print(tupleD)


# remove

state = ('MH', 'MP', 'UP', "RJ")
print(state)
# state = state.remove('MP')
# print(state)
state = list(state)
state.remove('MP')
print(state)
state = tuple(state)
print(state)


# delete

del state
# print(state)



# program 3
# unpacking

namesA = ('Ram', 'Sham', 'Sundar', 'Raju')
a = namesA[0]
print(a)
b = namesA[1]
print(b)
c = namesA[3]
print(c)


(a1,a2,a3,a4) = namesA
print(a1)
print(a2)
print(a3)
print(a4)


colors = ('red', 'black', 'green', 'blue')
(c1,c2,*c3) = colors
print(c1)
print(c2)
print(c3)

# loop

for ele in colors:
    print(ele)

for ele in range(len(colors)):
    # print(ele)
    print(colors[ele])


# methods

colors = ('red', 'black', 'green', 'blue', 'red')

x1 = colors.count('red')
print(x1)


x2 = colors.index('blue')
print(x2)


country = ("india","srilanka",'pakistan',"japan","india")
q = country.count("india")
print(q)

w = country.index("india",1)
print(w)



rev = ""
first_Name = "sarika"
for item in range(len(first_Name)):
    rev = first_Name[item] + rev
print(rev)