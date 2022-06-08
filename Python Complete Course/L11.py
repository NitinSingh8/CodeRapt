# Lecture 11

# dictionary : Unordered , mutable

# creating a dictionary

# create an empty dictionary
# dic = {}
# print(type(dic))

# dic = dict()
# print(type(dic))

# data = {"name": "Programmer"} # key always should be immutable

# How to access data from dictionary

# details = {"name":"Programmer" , "age":20 , "Location" : "India"}
#
# # 1. using a key
#
# print(details["Location"])
#
# # 2 get method
#
# print(details.get("country","Not present"))

#
# fruit_collection = {"apple":40, "banana":50, "pears" : 65 ,"watermelon" : 100}
#
# print(fruit_collection["apple"])
#
# # keys()
# print(fruit_collection.keys())
# print(type(fruit_collection.keys()))
#
# # values()
# print(fruit_collection.values())
# print(type(fruit_collection.values()))
#
# # items()
# print(fruit_collection.items())
# print(type(fruit_collection.items()))


# how to change the value in dictionary

# fruit_collection = {"apple":40, "banana":50, "pears" : 65 ,"watermelon" : 100}

# 1. Using key

# fruit_collection["apple"] = 50
# print(fruit_collection)

# 2. Using update method

# fruit_collection.update({"apple":50})
# print(fruit_collection)


# how to delete data from dictionary

# fruit_collection = {"apple":40, "banana":50, "pears" : 65 ,"watermelon" : 100}

# data = fruit_collection.popitem()
# print(data)
# print(fruit_collection)


# data = fruit_collection.pop("pears")
# print(data)
# print(fruit_collection)

# del fruit_collection["apple"]
# print(fruit_collection)

# fruit_collection.clear()
# print(fruit_collection)


# How to join two dictionary

# fruit_collection = {"apple":40, "banana":50, "pears" : 65 ,"watermelon" : 100}
# details = {"name":"Programmer" , "age":20 , "Location" : "India"}

# fruit_collection.update(details)
# print(fruit_collection)


# How to iterate over the dictionary

fruit_collection = {"apple":40, "banana":50, "pears" : 65 ,"watermelon" : 100}

# print(fruit_collection.items())

for key in fruit_collection.keys():  # dict_items([('apple', 40), ('banana', 50), ('pears', 65), ('watermelon', 100)])
    print(key, fruit_collection[key])