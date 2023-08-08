flowers = ['orchid', 'lily', 'rose', 'jasmine', 'lotus', 'daisy']

# Append -  add the last element in the list
flowers.append("Tulip")
print(flowers)

# clear -  clear list
flowers.clear()
print(flowers)

# copy one list to another list but updated existing list
fruits = ["apple","mango","banana"]
breakfast = fruits
breakfast[0] = "papaya"
print(fruits)
print(breakfast)


# Copy - copy one list to another list but not updated existing list
num = [10,20,30,40,50]
num2 = num.copy()
print(num2)
num2[1] = 22
print(num2)  # [10,22,30,40,50]
print(num) # [10,20,30,40,50]


# count - count the repetative elements in the list
num3 = [11,22,33,44,55,66,77,11,87,11]
a1= num3.count(11)
print(a1)

# extend - extend the existing list with another list
flowers = ['orchid', 'lily', 'rose']
print(flowers)
flowers1 = ['jasmine', 'lotus', 'daisy']
flowers.extend(flowers1)
print(flowers)


# index - return the index of the element
a2 = flowers.index('jasmine')
print(a2)


# insert - insert the element in the list on the specific position
flowers.insert(2, "Tulip")
print(flowers)

#pop -  remove the last element in the list & return removed element
a3 = flowers.pop()
print(a3)
print(flowers)


#remove - remove the element in the list on the specific position
flowers.remove('lotus')
print(flowers)


#reverse - reverse the list
flowers.reverse()
print(flowers)


#sort - sort the list with alphabetical order
flowers.sort()
print(flowers)

