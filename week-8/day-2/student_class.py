class Student:


    def greet(self):
        print(f"Your name is {self.name}")
        print(f"Your age is {self.age}")
        print(f"Your gender is {self.gender}")

    def getData(self, n, a, g):
        self.name = n
        self.age = a
        self.gender = g
        # self.city = "Surat"


s1 = Student()
# s1.getData("zaheer", 23, "male")
# s1.greet()
