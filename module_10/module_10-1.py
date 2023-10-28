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


# main program
elevator_1 = Elevator(1, 10)
elevator_1.go_to_floor(10)
print()
elevator_1.floor_up()
print()
elevator_1.floor_down()
print()
elevator_1.go_to_floor(elevator_1.bottom_floor)