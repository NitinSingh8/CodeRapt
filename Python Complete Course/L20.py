# Lecture 20

# Inheritance :
#
# class A
#
#
# class B


# class A: # Base Class  # Parent class
#     def a_method(self):
#         print("This is a A class method")
#
# class B(A): # Derived # child class
#     def b_method(self):
#         print("This is a B method")
#
#
#
# obj = B()
# obj.b_method()
# obj.a_method()

# inheritance means give all the right of public attribute and method to derived class

# Types :
# 5 types of inheritance
#
# 1. Single level
# 2. Multilevel
# 3.  Multiple
# 4. Hierarchical
# 5. Hybrid


class A: # Base Class  # Parent class
    def a_method(self):
        print("This is a A class method")

class B(A): # Derived # child class
    def b_method(self):
        print("This is a B method")

class C(A):
    def c_method(self):
        print("This is a C method")

class D(B,C):
    def d_method(self):
        print("this is a D method")

obj = C()
# obj.b_method()
obj.a_method()
obj.c_method()