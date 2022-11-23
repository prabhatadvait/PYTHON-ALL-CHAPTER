class Progammer:
    company = "Microsoft"
    def __init__(self,name,product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and product is {self.product}")
prabhat = Progammer("Prabhat","Macho") 
Randy = Progammer("Randy", "lux cozi")
prabhat.getInfo()
Randy.getInfo()