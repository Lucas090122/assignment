class Car:
    def __init__(self, rego, max_speed):
        self.registration_number = rego
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class ElectricCar(Car):
    def __init__(self, rego, mac_speed, battery):
        super().__init__(rego, mac_speed)
        self.battery_capacity = battery

class GasolineCar(Car):
    def __init__(self, rego, max_speed, volume):
        super().__init__(rego, max_speed)
        self.volume_of_tank = volume


# main program
electric_car = ElectricCar('ABC-15', 180, 52.5)
gasoline_car = GasolineCar('ACD-123', 165, 32.3)
electric_car.current_speed = electric_car.maximum_speed
gasoline_car.current_speed = gasoline_car.maximum_speed
# electric_car.travelled_distance = 0
# gasoline_car.travelled_distance = 0
electric_car.drive(3)
gasoline_car.drive(3)
print(electric_car.travelled_distance)
print(gasoline_car.travelled_distance)
