# sum(n) = sum(n-1) * n 
def sum_recursive(n):
    if n == 0 :
        return 0

    return n + sum_recursive(n-1)
a = sum_recursive(4)
print("sum of 4 ",str(a))

    