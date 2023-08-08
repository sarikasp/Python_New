# city = "pune"
# print(city)
# print(city[0])
#
#
# # program 2
# city2 = "malaysia"

#
# # program 3
#
# city3 = 'nagpur'
# city4 = """ hello """
# city5 = ''' helllo'''
#
# print(type(city3))
#
# # Type
# # Properties and Methods
# # Methods -- action and return
#
#
#
# city = "jaipur"
# q3 = len(city)
# print(q3)
#

#
#
# # program 4
# # upper
# q4 = city.upper()
# print(q4)
#
# # program 4
#
# city5 = "LUCKNOW"
# q5 = city5.lower()
# print(q5)
#
# # program 5
# q6 = city5.count("K")
# print(q6)
#
# #program 6
# q7 = city5.startswith("LUCK")
# print(q7)
#
# #program 7
# q8 = city5.endswith("nOW")
# print(q8)
#
# #program 8
# q9 = "sarika".lower().upper()
# print(q9)
#
# #program 9
#
# q10 = " jaipur "
# print(len(q10))
#
# q9 = q10.strip()
# print(q9)  # jaipur
# print(len(q9)) # 6
#
# # program 10
#
# info = "Sarika Shankar Pansare"
# q10 = info.split(" ")
# # ["Sarika","Shankar","Pansare"]
# print(q10)
#
#
# # program 11
# email = "pansaresarika@gmail.com"
# q11 = email.split('@')
# # ["pansaresarika","gmail.com"]
# print(type(q11))
# print(q11)
# #["p","yns","res","rik", "gm", "il.com"]
#
# # program 12
# info3 = "I am learning javascript"
# q12 = info3.replace("javascript","python")  # I am learning python
# print(q12)
#
# # program 13
# mks = "12"
# q13 = mks.isdigit() # True
# print(q13)
#
#
# # program 14
# mks2 = "adasdsa"
# q14 = mks2.isalpha() # True
# print(q14)
#
# # program 15
# mk3 = "A213213"
# q15 = mk3.isalnum()  # True
# print(q15)
#
# mk3 = "A213213 "
# q16 = mk3.isalnum()  # False
# print(q16)
#
#
# city = 'malaysia pune'
# print(city.capitalize())

# fibonacci series
num = int(input("How many Range of Number?"))
x, y = 0, 1
while y < num:
    print(y)
    x, y = y, x+y