class Taxi:
    def __init__(self, model, capacity, variant):
        self.__model = model
        self.__capacity = capacity
        self.__variant = variant

    def getModel(self):
        return self.__model

    def getCapacity(self):
        return self.__capacity

    def setCapacity(self, capacity):
        self.__capacity = capacity

    def getVariant(self):
        return self.__variant

    def setVariant(self, variant):
        self.__variant = variant

 
class Vehicle(Taxi):
    def __init__(self, model, capacity, variant, color):
        super().__init__(model, capacity, variant)
        self.__color = color

    def vehicleInfo(self):
        return self.getModel() + " " + self.getVariant() + " in " + self.__color + " with " + self.getCapacity() + " seats"


v1 = Vehicle("i20 Active", "4", "SX", "Bronze")
print(v1.vehicleInfo())
print(v1.getModel())
v2 = Vehicle("Fortuner", "7", "MT2755", "White")
print(v2.vehicleInfo())
print(v2.getModel())
