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


class Race:
    def __init__(self, name, kilometer, cars_list):
        self.race_name = name
        self.race_range = kilometer
        self.race_cars = cars_list

    def hour_passes(self):
        for car in self.race_cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        data = [("Plate", "Max speed", "Current speed", "Current distance")]
        data.extend([(car.registration_number, car.maximum_speed,
                      car.current_speed, car.travelled_distance) for car in
                     self.race_cars])
        print(tabulate(data, headers='firstrow', tablefmt='grid'))

    def race_finished(self):
        if max(car.travelled_distance
                  for car in self.race_cars) > self.race_range:
            return True


# main program
cars = []
for i in range(1, 11):
    cars.append(Car(f"ABC-{i}", random.randint(100, 200)))
new_race = Race("Grand Demolition Derby", 8000, cars)
hour = 0
while not new_race.race_finished():
    new_race.hour_passes()
    hour += 1
    if hour % 10 == 0:
        print(f"The race has been going on for {hour} hours, "
              f"and the current status is as follows.")
        new_race.print_status()
        print()
print(f"Race finished. The race took {hour} hours in total.")
champion = max(new_race.race_cars, key=lambda car: car.travelled_distance)
print(f"The champion is {champion.registration_number}")
new_race.print_status()