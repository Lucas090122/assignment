class Car:
    def __init__(self, rego, max_speed):
        self.registration_number = rego
        self.maximum_speed = max_speed

    current_speed = 0
    travelled_distance = 0

    def accerelate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed


# main program
new_car = Car("ABC-123", 142)
print(f"THe registration number of new car is {new_car.registration_number}, "
      f"the max speed of it is {new_car.maximum_speed} km/h, "
      f"current speed is {new_car.current_speed} km/h, "
      f"travelled distance is {new_car.travelled_distance} km.")
new_car.accerelate(+30)
new_car.accerelate(+70)
new_car.accerelate(+50)
print(f"The current speed of the car is {new_car.current_speed} km/h")
new_car.accerelate(-200)
print(f"The finial speed is {new_car.current_speed} km/h")