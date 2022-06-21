# Lecture 17

# Generator :

# def time():
#     print("Time is Morning")
#     yield 10
#
#     print("Time is Aftertoon")
#     yield 20
#
#     yield 30
# gen = time()
#
# print(next(gen))
# print(next(gen))
# print(next(gen))

#
# def even():
#     for i in range(20):
#         if i%2==0:
#             yield i
#
#
#
# for data in even(): # next()
#     print(data)



# Decorator :

def decorate(fun):
    def nested_fun():
        print("Name is ",end="")
        fun()
        print("This is new line ")
    return nested_fun

@decorate
def print_name():
    print("CodeRapt")

# print_name = decorate(print_name)


print_name() # output should be 'Name is CodeRapt'