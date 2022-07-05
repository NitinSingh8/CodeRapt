# Lecture 23


# Instance Methods : (can be called by object only)

# classmethod : can be called by only class

# static method :

class PrintName:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln

    def display(self): # instance methods
        print(f"first name is : {self.firstname} and last name is : {self.lastname}")

    @classmethod
    def only_name(cls,name):
        firstname , lastname = name.split() # Kapil , Singh
        return cls(firstname,lastname)
        # return obj

    @staticmethod
    def static_method(name):
        print("Name is ", name)

# PrintName.display()

# firstname = "Aditya"
# lastname = "Singh"
# obj = PrintName(firstname,lastname)
# obj.display()
#
#
# name = "Kapil Singh"
# obj2 = PrintName.only_name(name)
# obj2.display()

# PrintName.static_method("Aditya Singh")
obj3 = PrintName("Aditya","Singh")
obj3.static_method("Kapil Singh")