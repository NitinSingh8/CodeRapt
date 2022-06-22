# Lecture 18

# Recursion : function call itself

# def fun():
#     fun()
#
#
# fun()

# 5 = 5*4*3*2*1 = 120

# factorial by loop
#
# def factorial(num):
#     fact = 1
#
#     for i in range(1, num+1): # 1,2,3,4,5,...... num
#         fact *= i
#
#     return fact

def factorial(num): # 5
    # base condition
    if num<=1:
        return 1
    return num*factorial(num-1)

print(factorial(5))