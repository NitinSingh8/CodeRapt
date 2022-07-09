# Lecture 25

# getattr = X  --- age = 50

# syntax :
# getattr(object_name , attribute_name , default)



# setattr =
#
# synatx
# setattr(object_name, attribute_name, value)


# hasattr = present or not
# syntax :
# hasattr(object, attribute_name)


# delattr = delete an attribute in our class
# syntax :
# delattr(class , attribute)

class Person:
    per_age = 30
    per_name = "Neeraj"
    per_location = "India"
    per_height = 177

obj = Person()

# print(obj.per_age)

# print(getattr(obj, 'per_height',160))
# print(getattr(obj, 'per_age',20))
# setattr(obj, 'per_age',40 )
# print(getattr(obj, 'per_age',20))
# print(getattr(obj,'per_income'))
#
# setattr(obj, 'per_income' , 20000)

# print(getattr(obj,'per_income'))

# setattr(obj, 'per_income' , 20000)
# print(hasattr(obj,'per_income'))


print(hasattr(obj,'per_name'))
delattr(Person,'per_name')
print(hasattr(obj,'per_name'))