class Person:
    country = "India"

    def __init__(self):
        print("Intializing Person....")

    def takeBreath(self):
        print("I am breathing")

class Employee(Person):
    company = "Hero"

    def __init__(self):
        super().__init__()
        print("Intializing Employee")

    def getSalary(self):
        print(f"salary is {self.salary}")
    def takeBreath(self):
        super().takeBreath()
        print("I am breathing luckily because i am employee")
class Programmer(Employee):
    company = "Tata"

    def __init__(self):
        super().__init__()
        print("Intializing Programmer")

    def getSalary(self):
        print("No salary to programmers")
    def takeBreath(self):
        super().takeBreath()
        print("programmer is breathing not so heavily")
p = Person()
p.takeBreath()

e = Employee()
e.takeBreath()

pr = Programmer()
pr.takeBreath()
