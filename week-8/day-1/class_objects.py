"""
classes and objects
"""


class Student:
    # datamembers/attributes/varialbles
    name = ""
    age = 0
    gender = ""

    def greet(self):
        print("this is a greet method")
        print(f"your name is {self.name}")
        print(f"your name is {self.age}")
        print(f"your name is {self.gender}")

    def getData(self):
        self.name = input("Enter your name : ")
        self.age = int(input("enter your age : "))
        self.gender = input("enter gender : ")


s1 = Student()
s2 = Student()
# s1.name = "zaheer"
# s1.age = 23
# s1.gender = "Male"
# # print(s1.name)
# print(s1.age)
# print(s1.gender)
s1.getData()
s1.greet()
# s2.greet()
