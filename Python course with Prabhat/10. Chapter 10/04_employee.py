class employee:
    company = "Google"
    salary = 100

Aman = employee()
Rahul = employee()
print(Aman.company)
print(Rahul.company)
employee.company = "Amazon"
print(Aman.company)
print(Rahul.company)

