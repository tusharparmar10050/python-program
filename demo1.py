class School:
    __sname = "a2"
    # def __init__(self, age,__sname):
    #     self.age = age
    #     self.__sname = __sname
    #     # return self.age,self.__sname 

    def new(self):
        print("name is:", School.__sname)

class School_class(School):        
    def student(self):
        return self.age

# s1 = School_class(90)
# print(s1.age)

s2 = School()
s2.new()
