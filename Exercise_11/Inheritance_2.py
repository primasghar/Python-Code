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


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        self.battery = battery_capacity
        super().__init__(registration_number, maximum_speed)


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume,):
        self.tank_volume = tank_volume
        super().__init__(registration_number, maximum_speed)


def three_hour_race():
        electric_car = ElectricCar("ABC-15", 180, 52.5)
        change_of_speed_electric = random.randint(80, 180)

        gasoline_car = GasolineCar("ACD-123", 165, 32.3)
        change_of_speed_gasoline = random.randint(80, 165)
        drive_hour = 3

        electric_car.accelerate(change_of_speed_electric)
        electric_car.drive(drive_hour)
        print(f"Electric car drove {electric_car.travelled_distance} km in 3 hours.")

        gasoline_car.accelerate(change_of_speed_gasoline)
        gasoline_car.drive(drive_hour)
        print(f"Gasoline car drove {gasoline_car.travelled_distance} km in 3 hours.")



three_hour_race()