# Lecture 16

# Math module :

# import math
#
# print(math.pi)
#
# num = 6.5
#
# print(math.floor(num))
# print(math.ceil(num))
#
# print(math.factorial(10))
#
# # degree to radian
# print(math.radians(90))
#
# # radian to degree
# print(math.degrees(1.5707))
#
# # sin
# print(math.sin(math.radians(0)))



# String Module :

# import string as s
#
# # print(string.__doc__)
#
# print(s.ascii_lowercase)
#
# print(s.ascii_uppercase)
#
# print(s.ascii_letters)
#
# print(s.digits)
#
# print(s.printable)




# Random module

import random
#
# random.seed(10)
# print(random.random())
# print(random.random())
# random.seed()
# print(random.random())
# print(random.random())

# print(random.randint(1,100))

num = [10,20,30,40]

# print(random.choice(num))

# print(random.choices(num,k=3))

random.shuffle(num)

print(num)