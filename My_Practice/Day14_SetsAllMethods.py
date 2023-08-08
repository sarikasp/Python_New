nameA  = {"Sarika", "Gauri", "Sumit", "Chinmay", "Pallavi", "Sonali", "Swapnali", "Akash", "Sarika"}
print(nameA)
print(len(nameA))


# add()
nameA.add("Shivshree")
print(nameA)
print(len(nameA))


# # clear()
# nameA.clear()
# print(nameA)


# copy()
setC  =  {11,22,33}

# setD  = setC
# setC.remove(11)
# print(setC)  # {33, 22}
# print(setD)  # {33, 22}


setE  = setC.copy()
setE.remove(11)
print(setE)    # {33, 11, 22}
print(setC)    # {33, 22}


# difference()
setA = {11,22,33}
setB = {11,22,44}
print(setA.difference(setB))  # {33}
print(setB.difference(setA))  # {44}


# differenceUpdate()
setC = {11,22,33}
setD = {11,22,44}

print(setC.difference(setD))  # {33}
setC.difference_update(setD)  # {33}
print(setC)
#
#
# #discard()
# setR = {11,22,33,44}
# setR.discard(22)   # 22 removed
# print(setR)        # {33, 11, 44}
#
#
#interection()
setG = {11,22,33,44}
setH = {11,22,55,66}
print(setG.intersection(setH))    # {11,22}

# setG = {11,22,33,44}
# setH = {11,22,55,66}

# intersection_update()
setG.intersection_update(setH)    # {11,22}
print(setG)
#  setG = {11,22}


# #isdisjoint()
# setQ = {11,22,33}
# setH = {44,55,22}
# print(setQ.isdisjoint(setH))     # False
#
# setQ = {11,22,33}
# setH = {44,55,66}
# print(setQ.isdisjoint(setH))     # True

#
# #issuperset() #issubset()
# setI = {11,22,33}
# setH = {11,22}
# print(setI.issuperset(setH))    # True
# print(setH.issubset(setI))      # True
#
#
# # pop()
# setI.pop()
# print(setI)     # {11, 22}
#
#
# # remove()
# setI.remove(22)
# print(setI)       # {11}
#
#
# #union
# setQ = {11,22,33,44}
# setL = {44,55,66}
# setS = setQ.union(setL)
# print(setS)                 # {33, 66, 22, 55, 11, 44}
#
#
# #update()
# setQ.update({444,555})
# print(setQ)                       # {11,22,33,44,444,555}
# setQ.update([666,7777,88888])
# print(setQ)                      # {11,22,33,44,444,555,666,7777,88888}
#
#
# #symmetric difference()
# k = {1,2,3}
# l = {1,4,6}
# print(k.symmetric_difference(l))    # {2, 3, 4, 6}

# # symmetric_difference_update()
# k.symmetric_difference_update(l)
# print(k)                            # {2, 3, 4, 6}
# k = {2, 3, 4, 6}
