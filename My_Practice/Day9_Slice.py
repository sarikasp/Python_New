
#             0         1       2       3           4       5
flowers = ['orchid', 'lily', 'rose', 'jasmine', 'lotus', 'daisy']
#            -6        -5       -4     -3          -2     -1
print(flowers[1])
print(flowers[3])

# program 2
#flowers[startIndex:endIndex:steps]
print(flowers[1:])
print(flowers[-3:])
print(flowers[0:4])
print(flowers[1:4])
print(flowers[-4:4])
print(flowers[1:-1])
print(flowers[-1:-4])
print(flowers[0:len(flowers):2])
print(flowers[0:len(flowers):3])


# program 3
flowers = ['orchid', 'lily', 'rose', 'jasmine', 'lotus', 'daisy']
# print("orchid" in flowers)
#
# a1 = input("please enter the vegetable you wish to buy: ")
# if(a1 in flowers):
#     print('flower available')
# else:
#     print('flower not available')

# program 4
for flower in flowers:
    print(flower)

fruits = ["apple","mango","bananan","grapes"]

for  fruit in fruits:
    print(fruit)

# program 5
#
# for x in range(startIndex,endIndex,step):
#     print(x)

for x in range(10):
    print(x)

for x in range(1,10):
    print(x)

for x in range(2,22,2):
    print(x)

#             0         1       2       3           4       5
flowers = ['orchid', 'lily', 'rose', 'jasmine', 'lotus', 'daisy']
for x in range(len(flowers)):
    # print(x)
    print(flowers[x])