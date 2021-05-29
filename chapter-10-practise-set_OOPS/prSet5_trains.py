# Write a class Train which has methods to book a ticket, get status(no of seats), 
# and get fare information of trains running under Indian Railways.

class Train:
    
    def __init__(self,name,number,capacity):
        self.name   = name
        self.number = number
        self.capacity = capacity

    def bookTicket(self,passangerCount):
        if self.capacity >= passangerCount:
            print(f"Booked for {passangerCount} passangers.")
            print(f"now, {self.capacity - passangerCount} seats remains")
        else:
            print(f'sorry not enough seats available.')
    
    def getStatus(self):
        print(f'{self.capacity} seats available in {self.name}')       
    
    def fareInformation(self):
        print("Rajdhani Express = 1200")
        print("Doranto Express = 1100")
        print("Jan Stabdi Express = 1000")
        print("Garib Rath = 961")
        print("yashwanthpur Express = 750")
        print("Tapaswani Express = 890")


T1 = Train('yaswanthpur Express',212123,123)

T1.fareInformation()
T1.getStatus()
T1.bookTicket(4)
