# Lecture 5

# Conditional Statement :
# 1. IF
# 2. ELSE
# 3. NESTED IF
# 4. LADDER IF ELIF


#                    IF statement

# syntax
# if expression:
#     statement

#
# a = 10
# b = 5
#
# if a>b:
#     print("a is greater than b")
#     print("Hello CodeRapt")
#
# if a>b: print("a is greater than b"); print("Hello CodeRapt")



                    # ELSE statement

# a = 1
# b = 5

# if a>b:
#     print("a is greater than b")
# else:
#     print("a is not greater than b")

# short hand statement
# if a>b: print("a is greater than b")
# else: print("a is not greater than b")


                # NESTED IF


# if expression:
#     if expression:
#         if expression:


# a = 15
# b = 3
# c = 7

# Q. is a is greater than b and c ?

# if a>b: # True
#     if a>c: # True
#         print("a is greater than b and c")
#     else:
#         print("a is not greater than c")
# else:
#     print("a is not greater than b")


                # LADDER IF ELIF
#
# if expression:
#     statement
#
# elif expression:
#     statement
#
# elif expression:
#     statement
#
#     .....
#
# else:
#     statement


plane = 20000
train = 10000
bus = 5000

amount = 28000


# if plane>amount: # True
#     print("train")

if amount>=plane:
    print("I will go by plane")

elif amount>=train:
    print("I will go by train")

elif amount>=bus:
    print("I will go by bus")

else:
    print("I will not able to reach my destination")




