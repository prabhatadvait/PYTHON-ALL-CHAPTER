class Employee:
    company = "Google"
    salary = 100
    location = "Gaya"
    
    @classmethod
    def changeSalary(prabhat,sal):
        prabhat.salary = sal
  #   or we can also use below method to decorate the class attribute

    # def changeSalary(self,sal):
        # self.__class__.salary = sal    

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)

