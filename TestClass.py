class Car:
    def __init__(self, type):
        self.type = type

    # self parameter not needed if it is decleared static
    #@staticmethod
    def start(self):
        print("Car started...")
    
    # self parameter not needed if it is decleared static
    #@staticmethod
    def stop(self):
        print("Car stopped...")

class TataCar(Car):
    def __init__(self, name, price, type):
        super().__init__(type)
        self.name = name
        self.price = price
        super().start()

    @property
    def GST(self):
        return (self.price * 18)/100

car1 = TataCar("Tiago", 600000, "Electric")
print(car1.type)
print("GST: ", car1.GST)
car1.price = 800000
print("GST: ", car1.GST)
car1.stop()
del car1