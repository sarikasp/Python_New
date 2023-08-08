city = "pune"
print(city)
print(city[0])


# program 2
city2 = "chandrapur"
#0    1    2   3   4  5   6  7  8 9
# c   h    a   n   d  r  a  p   u  r

# program 3

city3 = 'nagpur'
city4 = """ hello """
city5 = ''' helllo'''

print(type(city3))

# Type
# Properties and Methods
# Methods -- action and return



city = "jaipur"
q3 = len(city)
print(q3)

# 0   1    2   3   4   5
# j   a    i    p   u   r


# program 4
# upper
q4 = city.upper()
print(q4)

# program 4

city5 = "LUCKNOW"
q5 = city5.lower()
print(q5)

# program 5
q6 = city5.count("K")
print(q6)

#program 6
q7 = city5.startswith("LUCK")
print(q7)

#program 7
q8 = city5.endswith("nOW")
print(q8)

#program 8
q9 = "chinmay".lower().upper()
print(q9)

#program 9

q10 = " jaipur "
print(len(q10))

q9 = q10.strip()
print(q9)
print(len(q9))

# program 10

info = "chinmay shirish deshpande"
q10 = info.split(" ")
# ["chinmay","shirish","deshpande"]
print(q10)


# program 11
email = "chinmaydeshpande@gmail.com"
q11 = email.split('@')
# ["chinmaydeshpande","gmail.com"]
print(type(q11))
print(q11)
#["chinm","ydeshp","nde@gm","il.com"]

# program 12
info3 = "I am learning javascript"
q12 = info3.replace("javascript","python")
print(q12)

# program 13
mks = "12"
q13 = mks.isdigit()
print(q13)


# program 14
mks2 = "adasdsa"
q14 = mks2.isalpha()
print(q14)

# program 15
mk3 = "A213213 "
q15 = mk3.isalnum()
print(q15)