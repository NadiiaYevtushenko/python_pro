import random
desired_distance = random.randint(0, 9)
race_dist = 0
winner = None

class Car:
    def __init__(self, fuel: int, trip_distance: int, model: str, color: str):
        self.fuel = fuel
        self.trip_distance = trip_distance
        self.model = model
        self.color = color

    def __repr__(self) -> str:
     return "<{}: fuel={} distance={}>".format(self.model, self.fuel, self.trip_distance)
    def move(self, distance: int) -> None:
        """Move the car to he given distance and decrease fuel but not more then fuel amount"""
        move_distance = distance if self.fuel >= distance else self.fuel


        self.trip_distance += move_distance
        self.fuel -= move_distance

chrysler = Car(random.randrange(0,9),0, "Chrysler", "white")
bmw = Car(random.randrange(0,9),0, "BMW", "black")
audi = Car(random.randrange(0,9),0, "Audi", "blue")

cars = [chrysler, bmw, audi]

while race_dist < desired_distance:
    distance = random.randrange(0,9)
    race_dist += distance
    for car in cars:
        car.move(distance)
        if car.trip_distance > desired_distance:
            winner = car
            print("Winner is {} with distance {}".format (winner.model, winner.trip_distance))
            break

print("\nRace finished!\n")
print("Results:")
for car in cars:
    print("{} drove {} and has {} fuel left".format(car.model, car.trip_distance, car.fuel))

