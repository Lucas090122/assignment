class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Reached floor {self.current_floor}")
        else:
            print("The elevator is on the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Reached floor {self.current_floor}")
        else:
            print("The elevator is on the bottom floor.")

    def go_to_floor(self, number):
        if number < self.current_floor:
            for _ in range(self.current_floor - number):
                self.floor_down()
        elif number > self.current_floor:
            for _ in range(number - self.current_floor):
                self.floor_up()
        else:
            print(f"The elevator is currently at {number} floor.")


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevator):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevator = number_of_elevator
        self.elevators = {}
        for i in range(self.number_of_elevator):
            self.elevators[i + 1] = Elevator(self.bottom_floor, self.top_floor)

    def run_elevator(self, elevator_number, destination_floor):
        self.elevators[elevator_number].go_to_floor(destination_floor)
        print(f"Elevator No.{elevator_number} "
              f"has reached floor {destination_floor}")


# main program
building_1 = Building(1, 10, 3)
building_1.run_elevator(1, 3)
building_1.run_elevator(2, 6)
building_1.run_elevator(3, 10)