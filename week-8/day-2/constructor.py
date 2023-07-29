class Student:
    def __init__(self):  # constructor
        # constructor is a method which is called whenever an object is created.
        self.name = input("Enter your name : ")
        self.age = int(input("enter your age : "))
        self.gender = input("enter gender : ")

    def __str__(self) -> str:
        return "you have printed object directly"

    # def __init__(self, n, a, g):
    #     self.name = n
    #     self.age = a
    #     self.gender = g

    def greet(self):
        print(f"Your name is {self.name}")
        print(f"Your age is {self.age}")
        print(f"Your gender is {self.gender}")


s1 = Student()
# s1.greet()
# s2=Student("zaheer",23,"male")
print(s1)
