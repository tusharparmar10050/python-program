class School:
    def __init__(self, sname, sclass, roll):
        self.__sname = sname
        self.__sclass = sclass
        self.__roll = roll

    def Getsname(self):
        return self.__sname

    def Getsclass(self):
        return self.__sclass

    def Setsclass(self, sclass):
        self.__sclass = sclass
    
    def Getroll(self):
        return self.__roll

    def Setroll(self, roll):
        self.__roll = roll


class Student(School):
    def __init__(self, sname, sclass, roll, age):
        super().__init__(sname, sclass, roll)
        self.__age = age
    def Studentinfo(self):
        return self.Getsname() + " in " + self.Getsclass() + " roll is " + self.Getroll() + " age is " + self.__age

s1 = Student("tushar", "12A", "45" , "19")
print(s1.Studentinfo())
print(s1.Getsclass())
