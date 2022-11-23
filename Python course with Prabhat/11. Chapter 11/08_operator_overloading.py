class Number:
    def __init__(self,num):
        self.num = num
    
    def __add__(self,num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self,num3):
        print("Lets multiply")
        return self.num * num3.num


n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
print(sum)
guna = n1 * n2
print(guna)