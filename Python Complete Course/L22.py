# Lecture 22

# Method Overloading : (having a same name but different parameter)



#
#
# def fun(a,b,c= None):
#     if c==None:
#         print(a,b)
#     else:
#         print(a,b,c)
#
# fun(2,4,7)



# Method Overriding

class A:
    def fun(self):
        print("This is a method of A class")

    def call(self):
        print("Call method")


class B(A):
    def fun(self):
        print("This is a method of B class")
    def fun2(self):
        print("this is a fun2 method")

    def call(self):
        print("CAll method in B class")
bobj = B()
# bobj.fun()
bobj.call()