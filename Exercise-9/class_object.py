class Car:
    def __init__(self, registration_number, maximum_speed, current_speed =0,travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self. current_speed = current_speed
        self.travelled_distance = travelled_distance

new_car = Car( "ABC-123", 142)

print(f"""Car details: 
        Registration number: {new_car.registration_number}
        Maximum speed: {new_car.maximum_speed} km/h
        Current speed: {new_car.current_speed} km/h
        Distance travelled: {new_car.travelled_distance}km")""")