class vehicle_904():
    def __init__(self,vehicleName, maxSpeed, vehicleAverage):
        self.name_of_vehicle = vehicleName
        self.max_speed = maxSpeed
        self.average_of_vehicle = vehicleAverage

class Car(vehicle_904):
    def seating_capacity(self, capacity):
        self.capacity = input("Enter seating capacity:")
        print(f"Vehicle Name: ",self.name_of_vehicle,"Seating Capacity: ",self.capacity)

vehicleObj = vehicle_904("Car","120","60")
obj = Car()
obj.seating_capacity()
