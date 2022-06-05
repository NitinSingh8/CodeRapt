# Lecture 10

# set = it contain unique data and it has unordered data

# Creating a set

# s = set()
# print(type(s))

# s = {"CodeRapt",45}
# print(type(s))
# print(s)

# can't create a set with mutable data type
# s = {"CodeRapt",100,[24,12]}
# print(s)

# Set methods
# how to add data in set

# add()
# s = {"CodeRapt",45}
# s.add(100.50)
# print(s)

# update
# s = {"CodeRapt",45}
# s.update(["Programmer",100])
# print(s)


s = {'CodeRapt', 'Programmer', 100, 45}
# remove()
# s.remove("Programmer")
# print(s)

# discard()
# s.discard("something")
# print(s)

# pop()
# s.pop()
# print(s)

# clear()
# s.clear()
# print(s)

# del s

# check whether data is present or not in set
# in ,not in

# if "something" in s:
#     print("Hello CodeRapt")

# Length of set
# print(len(s))

# Set Operation

# 1. Union
# 2. Intersection
# 3. Difference
# 4. Symmetric Difference

a = {1,2,3,4,5}
b = {3,4,5,6,7}

# Union
# c = a.union(b)
# c = a | b
# print(c)

# Intersection
# c = a.intersection(b)
# c = a & b
# print(c)

# Difference
# c = a.difference(b)
# c = a - b
# print(c)

# Symmetric Difference
# c = a.symmetric_difference(b)
c = a ^ b
print(c)