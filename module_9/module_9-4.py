import random
from tabulate import tabulate


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


# main program
cars = []
hour = 0
for i in range(1, 11):
    cars.append(Car(f"ABC-{i}", random.randint(100, 200)))
while max(car.travelled_distance for car in cars) < 10000:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
    hour += 1
print(f"The race took {hour} hours")
data = [("Plate", "Max speed", "Finial speed", "Finial distance")]
data.extend([(car.registration_number, car.maximum_speed,
              car.current_speed, car.travelled_distance) for car in cars])
print(tabulate(data, headers='firstrow', tablefmt='grid'))
champion = max(cars, key=lambda car: car.travelled_distance)
print(f"The champion is {champion.registration_number}")