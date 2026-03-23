# 3- Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators
# to the bottom floor. Continue the main program by causing a fire alarm in your building.

class Elevator:

    def __init__(self, bottom_floor, top_floor):
        if bottom_floor >= top_floor:
            print("Please enter a valid bottom floor number. It should be less than bottom floor")
        elif top_floor <= bottom_floor:
            print("Please enter a valid top floor number. It should be greater than bottom floor")

        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor_no):
        print(f"\nCurrently at floor:{self.current_floor}")
        print(f"Go to: {floor_no}\n")

        if floor_no > self.current_floor:
            print("Going Up")
            for x in range(self.current_floor, floor_no):
                self.floor_up()
                print(f"Floor {self.current_floor}")

        elif floor_no < self.current_floor:
            print("Going Down")
            for x in range(floor_no, self.current_floor):
                self.floor_down()
                print(f"Floor {self.current_floor}")

    def floor_up(self):
        self.current_floor = self.current_floor + 1

    def floor_down(self):
        self.current_floor = self.current_floor - 1

class Building:
    def __init__(self, building_bottom_floor, building_top_floor, total_elevators):
        self.building_bottom_floor = building_bottom_floor
        self.all_elevators =  []
        for x in range(total_elevators):
            self.all_elevators.append(Elevator(building_bottom_floor, building_top_floor))

        # print(f"{len(self.all_elevators)}")

    def run_elevator(self, elevator_no, destination_floor):
        building_elevators = len(self.all_elevators)
        if elevator_no <= building_elevators:
            self.all_elevators[elevator_no].go_to_floor(destination_floor)
            print(f"Elevator-{elevator_no} is at { self.all_elevators[elevator_no].current_floor} floor")
        else:
            print(f"{elevator_no} does not exist")

    def fire_alarm(self):
        i = 0
        print("Fire Emergency!!! All elevators are grounded. Please use stairs.")
        for elevator in self.all_elevators:
            i = i + 1
            elevator.current_floor = self.building_bottom_floor
            print(f"Elevator {i} is at {elevator.current_floor} floor now")



building_2 = Building(0,15,4)
building_2.fire_alarm()