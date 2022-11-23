class employee:
    company = "Google"
    def getsalary(self,signature):
        print(f"salary for this company {self.company} is {self.salary} and {signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")
    @staticmethod
    def time():
        print("Time is 9 AM now")
prabhat = employee()
prabhat.salary = 2897
prabhat.getsalary("Thanks") #employee.getsalary(harry)
prabhat.greet() #employee.greet()
prabhat.time()