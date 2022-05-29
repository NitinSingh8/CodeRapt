# Lecture 3

                        # TypeCasting
#
# Integer -> Float
# Float -> Integer
# String -> Float

# Typecasting -> 1. Implicit
#                2. Explicit

# implicit

# x = 4 # (int)
# y = 5.4 #(float)
#
# s = x+y
#
# print(s)
# print(type(s))

# Explicit TypeCasting

# 1. how to convert int to float and string
# 2. how to convert float to int and string
# 3. how to convert string to float and int
#
# 4. some exceptions(where we can get error)



# 1. how to convert int to float and string
# x = 4
#
# y = float(x)
# print(type(y))
#
# z = str(x)
# print(type(z))


# 2. how to convert float to int and string

# x = 4.5
#
# y = int(x)
# print(type(y))
#
# z = str(x)
# print(type(z))

# 3. how to convert string to float and int

# x = "345"
#
# y = float(x)
# print(type(y))
#
# z = int(x)
# print(type(z))

# 4. some exceptions(where we can get error)

# x = "24sdf323"
#
# y = int(x)
# print(type(y))


                # Input from User


# input() -> Always return a string

# Input as String
# name = input("Enter Your name : ")
#
# print(name)

# Input as an integer

# num = int(input("Enter a number : "))
# # value = int(num)
# print(type(num))
# print(num)


# Input as float

# num = float(input("Enter the value : "))
#
# print(type(num))
# print(num)


# Exception may occur

num = int(input("Enter some value : "))

print(num)