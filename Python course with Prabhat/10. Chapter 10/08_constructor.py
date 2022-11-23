class employee:
    company = "Google"
     
    def __init__(self,name,salary,subunit):
        print("remember that adhyatmik person cannot fall down")
        # we use below three line to intialize the object as ("prabhat",100,"youtube")
        self.name =name
        self.salary =salary
        self.subunit = subunit

    def getsalary(self,signature):
        print(f"salary for this company {self.company} is {self.salary} \n {signature}")
    
    def getDetails(self):
        print(f"name of the employee is {self.name}")
        print(f"salary of the employee is {self.salary}")
        print(f"subunit of the employee is {self.subunit}")
        
    @staticmethod
    def greet():
        print("Good Morning, Sir")
    @staticmethod
    def time():
        print("Time is 9 AM now")
prabhat = employee("Prabhat",100,"youtube")
# prabhat = employee() This throws an error -->
prabhat.getDetails()
