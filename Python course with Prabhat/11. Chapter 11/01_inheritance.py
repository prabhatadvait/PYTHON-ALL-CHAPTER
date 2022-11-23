class employee:
    company = "Google"
    def showDetails(self):
        print("This is an employee")
class Programmer(employee):
    Language = "Python"
    def getLanguage(self):
        print(f"This is the language {self.Language}")

    # def showDetails(self):
        # print("This is programmer")


e = employee()        
p = Programmer()
e.showDetails()
p.showDetails()
print(p.company)
p.getLanguage()
