class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing")

class Employee(Person):
    company = "Hero"
    def getSalary(self):
        print(f"salary is {self.salary}")
    def takeBreath(self):
        print("I am breathing luckily because i am employee")
class Programmer(Employee):
    company = "Tata"
    def getSalary(self):
        print("No salary to programmers")
    def takeBreath(self):
        print("programmer is breathing not so heavily")
p = Person()
p.takeBreath()
# print(p.company) #Throws an error
e = Employee()
e.takeBreath()
pr = Programmer()
print(pr.company)
pr.takeBreath()
print(pr.country)