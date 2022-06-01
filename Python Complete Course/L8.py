# Lecture 8

# List :-

# List is always mutable

# names = ["CodeRapt","Programmer",100,45.2]

# name1 = "CodeRapt"
# name2 = "Programmer"

                # Modify list with methods

# elements = ["CodeRapt","Programmer",100,45.2]

# append

# elements.append(50)
# print(elements)

#insert
# elements.insert(1,45)
# print(elements)

# Access list element
# print(elements[1])

# index
# print(elements.index(100))

# remove
# elements.remove("Programmer")
# print(elements)

# pop
# print(elements)
# elements.pop(1)
# print(elements)

# print(200 in elements)

# clear
# elements.clear()
# print(elements)

# name = ["first","Second"]
# extend

# elements.extend(name)
# print(elements)


                    # Slicing in list

# elements = ["CodeRapt","Programmer",100,45.2]
#
# new_data = elements[1:3]
# print(new_data)


                    # For loop in list and list comprehension

# data = [23,44,76,89,12]

# len()
# print(len(data))

# for i in data: # [23,44,76,89,12]
#     print(i)

# for i in range(0,len(data)):  # [0,1,2,3,4]
#     print(data[i])


num = list(range(21))
# print(num)

# get all even element from num list
# 1. By for loop
even_list = []
for i in num:
    if i%2==0:
        even_list.append(i)

print(even_list)

# 2. Using List comprehension

even_list_by_comp = [i for i in num if i%2==0]
print(even_list_by_comp)