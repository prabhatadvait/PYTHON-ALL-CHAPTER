# n!=1*2*3*4*...n
#n! = [1*2*3*n-1]!*n
# n!= (n-1)! * n 

# n = 4
# factorial = 1
# for i in range(n):
#     factorial = factorial * (i + 1)
# print(factorial)
def factorial_iter(n):
    factorial = 1
    for i in range(n):
      factorial = factorial * (i + 1)
    return factorial
print(factorial_iter(10))

def factorial_recursive(n):
  if n== 1 or n == 0:
    return 1
  else:
    return n * factorial_recursive(n-1)
f = factorial_recursive(5)
print(f)


