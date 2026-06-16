class Vehicle:
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100
class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        total_fare = base_fare + (base_fare * 0.10)
        return total_fare
if __name__ == "__main__":
    school_bus = Bus("School Volvo", 120, 15, 50)
    print(f"Vehicle Name: {school_bus.name}")
    print(f"Total Bus Fare: ${school_bus.fare():.2f}")