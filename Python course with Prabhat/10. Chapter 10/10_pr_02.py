class calculator:

    def __init__(self,number):
        self.number = number
    def square(self):
        print(f"The square of number {self.number} is {self.number**2}")
    def squareRoot(self):
        print(f"The square root of number {self.number} is {self.number**0.5}")
    def cube(self):
        print(f"The cube of number{self.number} is {self.number **3}")
prabhat = calculator(int(input("Enter the number")))
prabhat.square()
prabhat.cube()
prabhat.squareRoot()