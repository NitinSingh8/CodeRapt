# Lecture 24

# magical method : __ __ , __init__

#
# class Age:
#     def __init__(self,a):
#         self.age = a
#
#     def __str__(self):
#         return f"{self.age}"
#
# age_p1 = Age(30)
#
# # age_p1.display()
#
# print(age_p1)


# magical method for comparison

# class Data:
#     def __init__(self,x):
#         self.val = x
#
#     def __str__(self):
#         return f"{self.val}"
#
#     def __gt__(self,other):
#         return self.val>other.val
#
#     def __lt__(self,other):
#         return self.val<other.val
#
#
# obj1 = Data(10)
#
# # print(obj1)
#
# obj2 = Data(20)
# # print(obj2)
#
# # print(obj1>obj2)
# # print(obj2>obj1)
#
#
# print(obj1<obj2)
# obj1>obj2


# Operator overloading

class vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self,other):
        a  = self.i+other.i
        b  = self.j+other.j
        c  = self.k+other.k

        return vector(a,b,c)

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

v1 = vector(2,4,6)

# print(v1)

v2 = vector(1,3,5)

# print(v1)
# print(v2)

res_v = v1+v2

print(v1)
print(v2)
print(res_v)