# a = 32
# b = 46
# print("sum of a and b is: ",a+b)
class Number:
    def sum(self):
        return self.a + self.b
num = Number()
num.a = 12
num.b = 32
print(num.sum())   