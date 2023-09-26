class vehicle_904():
    def __init__(self,vehicleName, maxSpeed, vehicleAverage):
        self.name_of_vehicle = vehicleName
        self.max_speed = maxSpeed
        self.average_of_vehicle = vehicleAverage

class Car(vehicle_904):
    def __init__(self,vehicleName, maxSpeed, vehicleAverage,capacity):
        vehicle_904.__init__(self,vehicleName, maxSpeed, vehicleAverage)
        self.capacity = capacity
    def seating_capacity(self):
        print(f"Vehicle Name:",self.name_of_vehicle,",Seating Capacity: ",self.capacity)

obj = Car("Car",120,60,4)
obj.seating_capacity()
