class Vehicle():
    def __init__(self,name, max_speed, mileage,capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity=capacity
    def fare(self):
        return self.capacity * 100
class Bus(Vehicle):
    def fare(self):
        fare_bus = self.capacity * 100
        total_fare = fare_bus + (0.1 *fare_bus)
        return total_fare
    pass
class taxi(Vehicle):
    def fare(self):
        fare_taxi = self.capacity * 100
        return fare_taxi
    pass
car = Vehicle("Car",300, 14000,5)
print(car.name,car.max_speed, car.mileage)
School_bus = Bus("School bus", 200, 150,50)
print("\nVehicle Name:", School_bus.name, "\nSpeed:", School_bus.max_speed, "\nMileage:",
School_bus.mileage,"\nCapacity:",School_bus.capacity)
print("Total Bus fare is:", School_bus.fare())
Taxi = taxi("cab", 300, 180,3)
print("\nVehicle Name:", Taxi.name, "\nSpeed:", Taxi.max_speed, "\nMileage:",
Taxi.mileage,"\nCapacity:",Taxi.capacity)
print("Total taxi fare is:", Taxi.fare())
pic_fare=((School_bus.fare()*50)/100)+((Taxi.fare()*3)/100)
print("\nTotal picnic fare:",pic_fare)