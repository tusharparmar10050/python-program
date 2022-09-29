
class Student:
    def result(self):
        if self.marks >= 40:
            return True
        else:
            return False
    # def __init__(self, name , marks):
    #     self.name=name
    #     self.marks=marks

student1 = Student(input("Enter name:"),int(input("enter marks")))
print(student1.name)
print(student1.marks)
did_pass = student1.result()
print(did_pass)



