# n! = 1 X 2 X 3 X ...n

num = int(input("Enter the number:- "))
factorial = 1
for i in range (1,num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")
