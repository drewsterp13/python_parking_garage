# This is a class, where it can have a lot of uses, such as one class running the commands,
# another class runs the acual tools, another class runs the user interface. A class is a way
# to organize your code into smaller parts.
# This class runs the tools
class ParkingGarage():
    
# tickets and parkingSpaces are lists
# currentTicket is a dictionary
    
    # __init__ Method, where you can enter variables, called "attributes", from outside of the class
    # into the class, has to use the keywork: self
    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
        self.ticket_number = 0
        self.parking_number = 0
        self.user_price = 0
    
    # This is a class method, it is simular to a function, execpt it runs inside
    # a class and has to be called on.
    def takeTicket(self):
        self.ticket_number = self.tickets.pop(-1)
        self.parking_number = self.parkingSpaces.pop(-1)
    
    # Class Method
    def payForParking(self):
        self.user_price = int(input("\nHow much do you want to pay? "))
        if self.user_price > 0:
            print("\nYour ticket has been paid, you have 15 minutes to leave.")
            self.currentTicket["paid"] = True
    
    # Class Method
    def leaveGarage(self):
        if self.user_price > 0:
            print("\nThank You, have a nice day")
        else:
            print("\ndNOTICE: You have not paid yet!")
            while True:
                self.user_price = int(input("How much do you want to pay? "))
                if self.user_price > 0:
                    print("Thank you, have a nice day!")
                    self.tickets.append(self.ticket_number)
                    self.parkingSpaces.append(self.parking_number)
                    break
                else:
                    print("Sorry, we don't except 0, please enter a higher number")

# This instanitates the class, for now on, it will be refered as "parking_garage"
# Also, note that the lists are automaticlly generated.
parking_garage = ParkingGarage([i for i in range(20)], [j for j in range(20)], {})

#This class controls the user interface of the program
class Control():
    # This method runs the program
    def userInput(x):
        while True:
            print("Welcome to the parking garage, here is your ticket")
            parking_garage.takeTicket()
            parking_garage.payForParking()
            parking_garage.leaveGarage()
            print('Enter "quit" if you want to leave, any other key, you revisit the parking garage')
            input_keyword = input("ENTER HERE: ")
            if input_keyword == "quit":
                break

ctrl = Control() #This is instanitating, were for now on, we use the term
# "ctrl" instead of "Control()"
ctrl.userInput()