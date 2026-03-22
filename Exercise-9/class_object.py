class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0,travelled_distance = 0):
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


# new_car = Car( "ABC-123", 142)
#
# print(f"""Car details:
#         Registration number: {new_car.registration_number}
#         Maximum speed: {new_car.maximum_speed} km/h
#         Current speed: {new_car.current_speed} km/h
#         Distance travelled: {new_car.travelled_distance}km")""")

# new_car.accelerate(30)
# new_car.accelerate(70)
# new_car.accelerate(50)
# print(f"current speed: {new_car.current_speed} km/h")
# new_car.accelerate(-200)
# print(f"current speed: {new_car.current_speed} km/h")


# Solution check for part 3
new_car1 = Car( "ABC-123", 142, 60, 2000 )

print(f"""Car details: 
        Registration number: {new_car1.registration_number}
        Maximum speed: {new_car1.maximum_speed} km/h
        Current speed: {new_car1.current_speed} km/h
        Distance travelled: {new_car1.travelled_distance}km")""")
new_car1.drive(1.5)
print(f"new car distance: {int(new_car1.travelled_distance)} km")