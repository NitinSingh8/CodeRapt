# Lecture 13

# Local variable : limited to block
# Global variable : access anywhere in program

# local variable
# def fun():
#     name = "Programmer"
#     print("In fun , name is ",name)
#
# fun()
# print("In global scope , name is ",name)


# global variable

# name = "CodeRapt"
#
# def fun():
#     # name is programmer inside this function anywhere
#     name = "Programmer"
#     print("In fun, name is ",name)
#
# fun()
#
# print("In global scope name is ", name)




# x = 50
#
# def fun():
#     global x
#     x+=50
#     print("in fun x is ", x)
#
# print("before calling fun x is ", x)
# fun()
# print("after calling fun x is ", x)

x = 100

def fun():
    x = 40
    def nested_fun():
        nonlocal x
        x = 50
        print("inside of nested fun x is ", x) # 50

    nested_fun()
    print("in fun value of x is ", x) # 40

fun()

print("in global scope the value of x is ", x)