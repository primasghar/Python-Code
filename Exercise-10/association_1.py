# 1- Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
# The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor.
# If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or
# floor_down methods as many times as it needs to get to the fifth floor. The methods run the elevator one floor up
# or down and tell what floor the elevator is after each move. Test the class by creating an elevator in the
# main program, tell it to move to a floor of your choice and then back to the bottom floor.

class Elevator:

    def __init__(self, bottom_floor, top_floor ):
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
            for x in range( self.current_floor, floor_no):
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



h = Elevator(0,15)

h.go_to_floor(3)
h.go_to_floor(0)
h.go_to_floor(9)
h.go_to_floor(4)



