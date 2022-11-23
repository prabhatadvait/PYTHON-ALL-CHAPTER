class Employee:
    company = "Google"
    salary = 100
Ram = Employee()
Laksham = Employee()

# Creating instances attribute salary for both objects
# Ram.salary = 290
# Laksham.salary =299
Ram.salary = 290
print(Ram.salary)
print(Laksham.salary)
#Below line will throw an error because because object is not present in instance/class object

print(Ram.address) 
