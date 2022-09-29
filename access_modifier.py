# -----------------------------Public-----------------------------------
class student:
    def __init__(self, sname, age):
        self.SName = sname
        self.Age = age


class display(student):
    def __init__(self, sname, age):
        super().__init__(sname, age)

    def dispalyAge(self):
        print("age of student is:", self.Age)
        print("Name of student is:", self.SName)


obj = display("Ram", 17)

obj.dispalyAge()
# # -----------------------------Protected--------------------------------
# defining a class Employee


class Employee:
    # constructor
    def __init__(self, name, sal):
        self._name = name   # protected attribute
        self._sal = sal    # protected attribute
        print("Name:", self._name, "salary:", self._sal)


class HR(Employee):

    # member function task
    def task(self):
        print("We manage Employees")


emp = HR("Captain", 10000)
# emp._sal
emp.task()

# -----------------------------Private----------------------------------
# defining class Employee


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


s1 = Student("tushar", "12A", "45", "19")
print(s1.Studentinfo())
print(s1.Getsclass())
