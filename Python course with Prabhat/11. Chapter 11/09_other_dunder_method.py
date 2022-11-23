class Number:
    def __init__(self,num):
        self.num = num
    
    def __add__(self,num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self,num3):
        print("Lets multiply")
        return self.num * num3.num
    
    def __str__(self):
        return f"Decimal Number:{self.num}"

    def __len__(self):
        return self.num #or return 2

n = Number(9)
print(n)
print(len(n))
        