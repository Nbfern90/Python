# attributes = What make up the car
# methods-what the car can do
class Car():

    year = 2020

    all_cars = []

    def __init__(self, color, flames):
        self.model = "Tesla"
        self.color = color
        self.flames = flames
        self.is_running = False
        self.in_one_piece = True

        Car.all_cars.append(self)

    def start_car(self):
        print("Vroom! I am on.")
        self.is_running = True

    def self_destuct(self):
        print("Boom!")
        self.in_one_piece = False

    @classmethod  # this method targets all instaces in the class
    def all_destuct(cls):
        for car in cls.all_cars:
            car.self_destuct()


patricks_car = Car('red', 'green')
vinces_car = Car('blue', 'white')


vinces_car.start_car()
vinces_car.self_destuct()

print(vinces_car.is_running)

Car.year = 2019  # this would change all the instances in the class, because this targets the CLASS ATTRIBUTE

print(Car.all_destuct())
