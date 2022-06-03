# Lecture 9

# Tuple :- It is immutable

# create a tuple

# tup = tuple()
# print(tup)

# tup = ("CodeRapt",45)
# print(tup)

# tup = ("CodeRapt",)
# print(tup)
# print(type(tup))

# Access data from tuple

# tup = (10,20,30,40,50)
# print(tup[2])
# print(tup[-3])
# print(tup.index(30))


# slicing in tuple
# tup = (10,20,30,40,50)
#
# print(tup[1:4])
# print(tup[:4:2])

# tup = (10,20,30,40,50)
# print(len(tup))

# unpacking and packing in tuple
# unpacking
# tup = (4,9,11)
# even,odd,prime = (4,9,11)
# even = tup[0]
# odd = tup[1]
# prime = tup[2]

# print(even,odd,prime)
#packing
# tup = "CodeRapt" , 45, 543.34
# print(tup)
# print(type(tup))

# for loop in tuple
# using value

# tup = (10,20,30,40,50)
# for data in tup:
#     print(data)

#using index

# tup = (10,20,30,40,50)
# for i in range(0,len(tup)): # [0,1,2,3,4]
#     print(tup[i])

# concatenate tuple
# tup1 = (2,4,6,8)
# tup2 = (1,3,5,7)

# 1. using + operator
# tup3 = tup1 + tup2
# print(tup3)

# 2. sum method

# tup3 = sum((tup1,tup2),())
# print(tup3)

# Nested tuple

tup1 = (10,20,30)
tup2 = (40,50,60)
tup3 = (70,80,90)

tup = (tup1,tup2,tup3)

for data in tup: # (tup1,tup2,tup3)
    print(data)
    # print()
