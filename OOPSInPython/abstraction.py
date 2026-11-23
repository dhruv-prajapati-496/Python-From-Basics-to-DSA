# Abstraction : Hiding the implementation details and showing only necessary data to the users
class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    # to start the car
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started")

    # to stop the car
    def stop(self):
        self.clutch = True
        self.brk = True
        self.acc = False
        print("Car stopped")

car1 = car()
car1.start()
car1.stop()

# In this program, user can only see, car started and car stopped nothing else, all the implementation details are hidden and this is called abstraciton       