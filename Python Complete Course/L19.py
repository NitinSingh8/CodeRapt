# Lecture 19

# class :


# attribute :
# method:
# constructor :


class Person :

    def __init__(self,n,a,p):
        # print("Constructor of Person class created")
        self.name = n
        self.age = a

        # private attribute
        self.__password = p

    def print_data(self):
        print("name is : ",self.name)
        print("age is : ", self.age)


# obj = Person()
# # print(obj.name)
# # print(obj.age)
# # obj.name = "CodeRapt"
# # obj.age = 20
# obj.print_data()
#
# obj2 = Person()
# obj2.print_data()

# obj = Person("CodeRapt",20)
# obj.print_data()
#
# obj2 = Person("Programmer",22)
# obj2.print_data()


obj = Person("CodeRapt",20,12345)

print(obj.name)
print(obj.age)
# print(obj.__password)
# print(obj._Person__password)