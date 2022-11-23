class Train:
    def __init__(self,name,seats,fare):
        self.name = name
        self.seats = seats
        self.fare = fare
    def getStatus(self):
        print(f"The available seats in this train is {self.seats}")

    def fareInfo(self):
        print(f"Train no:- 34353 will set off Banglore and price is Rs {self.fare}")
        print(f"The name of the train is {self.name}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"your seat no is {self.seats}")
            self.seats = self.seats-1
        else:
            print(f"Sorry seat is not availabe! Go for tatkal")
prabhat = Train("Sanghmitra",90,2448) 
prabhat.fareInfo()
prabhat.getStatus()
prabhat.bookTicket()
prabhat.getStatus()