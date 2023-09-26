class vehicle_904():
    def __init__(self,vehicleName, maxSpeed, vehicleAverage):
        self.name_of_vehicle = vehicleName
        self.max_speed = maxSpeed
        self.average_of_vehicle = vehicleAverage

    def displayValues(self):
        print(f"Vehicle's name is: ",self.name_of_vehicle)
        print(f"Vehicle's maximum speed is: ",self.max_speed)
        print(f"Vehicle's average speed is: ", self.average_of_vehicle)

vehicleObj = vehicle_904("Car","120","60")
vehicleObj.displayValues()