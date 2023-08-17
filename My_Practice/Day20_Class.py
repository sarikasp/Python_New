class Person:
    age = 25
    fullName = 'Sarika Pansare'
    rollNo = 31

    def talk(self):
        print('I am Talking')

    def walk(self):
        print('I am Walking')

sarika = Person()
print(sarika.fullName)
print(sarika.age)
print(sarika.rollNo)
print("-------- ------------- ---------- -------- --------- -------------")

sarika.talk()
sarika.walk()
print("-------- ------------- ---------- -------- --------- -------------")

sumit = Person()
print(sumit.fullName)
print(sumit.age)
print(sumit.rollNo)
print("-------- ------------- ---------- -------- --------- -------------")

sumit.talk()
sumit.walk()
print("-------- ------------- ---------- -------- --------- -------------")

sumit.age = 31
sumit.fullName = 'Sumit Malunjkar'
sumit.rollNo = 20

print(sumit.age)
print(sumit.fullName)
print(sumit.rollNo)

print("-------- ------------- ---------- -------- --------- -------------")

# program 2

class Person2:

    def __init__(self, fn, ag, rn):
        self.fullName = fn
        self.age = ag
        self.rollNo = rn

    def display(self):
        print(self.fullName)
        print(self.age)
        print(self.rollNo)


sarika = Person2('Sarika Pansare', 25, 40)
sarika.display()
print("-------- ------------- ---------- -------- --------- -------------")

sumit = Person2('Sumit Malunjkar', 31, 25)
sumit.display()





