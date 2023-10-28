class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"


class Autobus(Transport):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


bus = Autobus("Renaul Logan", 0, 0)
print(bus.seating_capacity())
