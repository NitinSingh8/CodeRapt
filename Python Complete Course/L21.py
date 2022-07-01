# Lecture 21

# Polymorphism : (having a same but different behaviour)

# len()

# string = "CodeRapt"
# li = [12,14,15,20]
#
# print(len(string))
# print(len(li))


# 1. Polymorphism with function

# def fun(a = 0,b=0,c=0):
#     print(a+b+c)
#
#
# fun()
# fun(100)
# fun(1,2,3)


# 2. Polymorphism in class

class Company:
    def address(self):
        print("Address of a company is : ABC")

class Employee(Company):
    def address(self):
        print("Address of employee is : XYZ")



obj = Employee()
obj.address()