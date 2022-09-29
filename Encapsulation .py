# Python program to
# demonstrate private members

# Creating a Base class


class Base:
    # def demo(self, c):
    #     self.__c = c

    def __init__(self):
        self.a = "GeeksforGeeks1"

    def demo(self):
        # self.__c = c
        self.__c = "GeeksforGeeks2"
        return self.__c


# Creating a derived class


class Derived(Base):
    def __init__(self):

        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)



# Driver code
obj1 = Base()
print(obj1.a)
# obj2 = Derived()    # class derived classes	    
print(obj1.demo())  

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
