# Lecture 14

# lambda
# map
# filter


# lambda :

# def l(x):
#     return x**2

# print( (lambda x : x**2) (10))

# s = lambda x,y : x+y
#
# print(s(3,5))


# map :
# (arg1, arg2) # arg1 = function , object (iterable)

# num = [2,6,3,9,12,15]

# way -1
# def fun(x):
#     return x+5

# new_num = []
# for data in num:
#     new_num.append(fun(data))

# way -2
# new_num = list(map(lambda x : x+5,num))
#
# print(new_num)


# filter :
# (arg1, arg2)

num = [2,6,3,9,12,15]

# def fun(x):
#     return x%2==0 # True if even else False

new_num = list(filter(lambda x:x%2==0,num))
print(new_num)


Task:
1. [1,2,3,4,5,6,7,8,9,10]
    x*5+7
    [12,17,.....]

