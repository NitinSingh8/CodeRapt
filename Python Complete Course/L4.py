# Lecture 4

# Operators :
#
# 1. Airthmetic
# 2. Relational
# 3. Assignment
# 4. Logical
# 5. Membership
# 6. Identity
# 7. Bitwise


# 1. Airthmetic Operator

# +  -   *   /    //  % **

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
#
# print(a+b)
# print(a*b)
# print(a-b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)


# 2. Relational Operator -> Return (True / False)

# < , > , <=  , >= , == , !=

# print(a<b)
# print(a>b)
# print(a <= b)
# print(a>=b)
# print(a==b)
# print(a!=b)


# 3. Assignment Operator

# +=  -=   *=   /=    //=  %= **=

# 4. Logical Operator

# and , or , not
#
# and -> if both operand will be true then only return true
# (True and True) -> True
# (False and True) -> False
#
# or -> if any of the value is True then return True
# (True or False) -> True
# (False or True) -> True
# (True or True) -> True
#
# not -> if input = True then return False
#        if input = False then return True

# print(True and False)
# print(True or False)
# print(not False)

# 5. Membership Operator

# in , not in
#
# "5" in "3423546"  -> if left operand is present in right operand
#                     then return True else False


# print("5" not in "23452034")

# 6. Identity Operator
# a = 3
# b = a
#
# # is , not is
#
# print(b is not a)

# 7. Bitwise Operator

# &  , | , ^ , ~ , << , >>

# 10 ->  0 1 0 1 0
# 5 ->   0 0 1 0 1
       # 0 1 1 1 1

print(10&5) # 0
print(10|5) # 15
print(10^5) # 15
print(~5) # -6
print(2<<3)  # 2 * (2**3) = 2 * (8) = 16
print(8>>2)  # 8 /  ( 2**2) = 8 / 4 = 2
