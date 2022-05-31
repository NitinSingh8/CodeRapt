# Lecture 6

# Loop :

# types of loop: 1. For loop    2. while loop      3. Nested loop


# range()
#
# range(start,end/stop,step_size)
#
# start
# end
# step_size = skip value
#
# range(2,7,1)
# 2,3,4,5,6
#
# range(0,10,1)
# 0,1,2,3,4,5,6,7,8,9
#
# range(1,6,2)
# 1,3,5


# syntax :
# for var in sequence:
#     print("dfls")
    # code

# for i in range(0,10):  # [0,1,2,3,4,5,6,7,8,9]
#     print("name")
#
# for i in range(0,10):  # [0,1,2,3,4,5,6,7,8,9]
#     # print(i)
#     if i%2 ==0:
#         print(i)



# 2. While Loop

# syntax:
#
# while expression:
#     code
#     update condition

# a = 0
# while a<10:
#     print(a) # 0 # 1 # 2 # 9
#     a = a+1  # a = 10
#
# else:
#     print("Your condition is get False")
#

# 3. Nested Loop

# # loop:
#     loop:
#      loop:

# 1
# 1 2
# 1 2 3
# 1 2 3 4

# for i in range(1,5): # 1,2,3,4
#     a = 1
#     while a<i+1:
#         print(a,end = " ")
#         # a = a+1
#         a+=1
#     print()


                # LOOP CONTROL STATEMENT

# 1. Break
# 2. Continue
# 3. Pass


# Break
#
# break

# for i in range(10): # [0,1,2------9]
#     print(i)
#     if i==5:
#         break

# Continue
# continue

# for i in range(10):
#     if i%2==0:
#         continue
#     print(i)

# a = 0
# while a<10:
#     if a%2==0:
#         a += 1
#         continue
#     print(a)
#     a+=1


# Pass Statement

# pass
print("Hello")

for i in range(10):
    pass

print("CodeRapt")

