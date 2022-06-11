# Lecture 12

# function :

# syntax :
#
# def function_name(argument):
#     body
#
#     return None by default


# function without argument
def fun():
    print("This is a function with name fun and have no argument")


# fun()

# function with argument

def fun_with_argument(name):
    print("This is a function with name fun_with_argument and have one argument")
    print("name is : ",name)

# fun_with_argument("CodeRapt")


# def add(a,b):
#     c = a+b
#
#     return c
#
# first = int(input("Enter first number : "))
# second = int(input("Enter second number : "))
#
# sum = add(first,second)
#
# print("sum is : " , sum)


# different ways to use argument while calling the function

# 1. positional argument
#
# 2. keyword argument

# def add(a,b):
#     print("a ", a)
#     print("b ", b)
#     c = a+b
#     return c
#
# first = int(input("Enter first number : "))
# second = int(input("Enter second number : "))
#
# sum = add(a= first ,b= second)
#
# print("sum is : " , sum)


# 3. default argument
#
# def add(b,a=50):
#     print("a ", a)
#     print("b ", b)
#     c = a+b
#     return c
#
# first = int(input("Enter first number : "))
# second = int(input("Enter second number : "))
#
# sum = add(first,second)
#
# print("sum is : " , sum)


# 4. variable length argument ( * )

def add(*data): # data is tuple = ()
    # body
    print(data)
    c = sum(data)

    return c

print(add(5))

print(add(2,5))

print(add(4,5,6,7))



Task :

1. write a function which should return maximum number out of three number

2. write a function that take n integer argument and return mutliplication of all these argument