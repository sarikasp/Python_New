flowers = ['orchid', 'lily', 'rose', 'jasmine', 'lotus', 'daisy']

# append()
flowers.append('tulip')
print(flowers)

# # clear()
# flowers.clear()
# print(flowers)

# copy()
flower = flowers.copy()
print(flower)
flower[1] = 'tulip'
print(flower)
print(flowers)


# count()
flowers1 = ['orchid', 'lily', 'rose', 'jasmine', 'lotus', 'daisy', 'orchid']
a1 = flowers1.count('orchid')
print(a1)

# index()
a2 = flowers1.index('jasmine')
print(a2)

# extend()
flowers2 = ['orchid', 'lily', 'rose']
flowers3 = ['jasmine', 'lotus', 'daisy', 'orchid']
# flowers2.extend(flowers3)
# print(flowers2)

# insert()
flowers2.insert(3, 'daisy')
print(flowers2)

# pop()
a4 = flowers2.pop()
print(a4)
print(flowers2)
flowers2.pop(0)
print(flowers2)

# remove()
flowers3.remove('lotus')
print(flowers3)

# reverse()
flowers.reverse()
print(flowers)

# sort()
flowers.sort()
print(flowers)