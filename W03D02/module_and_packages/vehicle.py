import logging


class Vehicle:
    def __init__(self, name):
        self.name = name
        self.speed = 0

    def increase_speed(self, speed):
        self.speed += speed

    @classmethod
    def log_entry(cls, vehicle_obj):
        logging.info(f"New Vehicle Added {vehicle_obj.name}")


class Car(Vehicle):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

    def accelerate(self):
        print('Wohooomm.........')
        self.increase_speed(50)
