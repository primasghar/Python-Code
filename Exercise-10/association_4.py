
# 4-This exercise continues the previous car race exercise from the last exercise set. Write a Race class that has
# the following properties: name, distance in kilometers and a list of cars participating in the race.
# The class has an initializer that receives the name, kilometers, and car list as parameters and sets
# their values to the corresponding properties in the class. The class has the following methods:
#
#--hour_passes, which performs the operations done once per hour in the original exercise: generates a random
# change of speed for each car and calls their drive method.

# --print_status, which prints out the current information of each car as a clear, formatted table.

# --race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the
# entire distance of the race.

# Write a main program that creates an 8000-kilometer race called Grand Demolition Derby.
# The new race is given a list of ten cars similarly to the earlier exercise. The main program simulates the
# progressing of the race by calling the hour_passes in a loop, after which it uses the race_finished method to
# check if the race has finished. The current status is printed out using the print_status method every ten hours
# and then once more at the end of the race.

import random

class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self. current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change_speed):
        new_speed =  self.current_speed + change_speed

        if new_speed < 0:
            self.current_speed = 0

        elif new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed - 1

        else:
            self.current_speed = new_speed
    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance = self.travelled_distance + distance


class Race:
    def __init__(self, name, distance, cars_list_no ):

        self.name = name
        self.distance = distance
        self.cars_list = []
        for i in range(1, cars_list_no+1):
            reg_no = f"ABC-{i}"
            max_speed = random.randint(100, 200)

            car = Car(reg_no, max_speed)
            self.cars_list.append(car)

    def hour_passes(self):
        for carNumber in range(len(self.cars_list)):
            change_of_speed = random.randint(-10, 15)
            drive_hour = 1

            self.cars_list[carNumber].accelerate(change_of_speed)
            self.cars_list[carNumber].drive(drive_hour)

    def print_status(self):
        table_headings = [["Registration No", "Maximum Speed", "Current Speed", "Distance Travelled"]]
        for row in table_headings:
            print("{: >20} {: >20} {: >20} {: >20}".format(*row))

        for carNumber in range(len(self.cars_list)):
            registration_number = f"{self.cars_list[carNumber].registration_number}"
            maximum_speed = f"{self.cars_list[carNumber].maximum_speed} km/h"
            current_speed = f"{self.cars_list[carNumber].current_speed} km/h"
            distance_travelled = f"{self.cars_list[carNumber].travelled_distance} km"

            table_data = [[registration_number, maximum_speed, current_speed, distance_travelled]]
            for row in table_data:
                print("{: >20} {: >20} {: >20} {: >20}".format(*row))

    def race_finished(self):
        for carNumber in range(len(self.cars_list)):
            if self.cars_list[carNumber].travelled_distance >=  self.distance:
                print(f"Congratulations! {self.cars_list[carNumber].registration_number}, you are the winner of {self.name} race with {self.cars_list[carNumber].travelled_distance} km drive.")
                return True
        return False




car_race = Race("Grand Demolition Derby", 8000, 10)

while not car_race.race_finished():
    for i in range(10):
        car_race.hour_passes()

    print(f"10 hours status")
    car_race.print_status()

car_race.print_status()


















