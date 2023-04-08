# Exercise 1
# --------------------

class Car:
    headlights_count = 4
    left_wheel = True
    wheels_count = 4

    def __init__(self, horsepower, weight, engine_type):
        self.horsepower = horsepower
        self.weight = weight
        self.engine_type = engine_type

    def max_speed(self):
        return self.horsepower / self.weight * 1500


    @classmethod
    def change_wheel(self):
        self.left_wheel = False

    @staticmethod
    def change_wheel_static():
        Car.left_wheel = False



cls = Car(585, 2111, "5.5-liter twin-turbo V-8")
m5 = Car(635, 1851, "4.4-liter twin-turbo V-8")


print(cls.max_speed())
print(m5.max_speed())

# --------------------




# Exercise 2
# --------------------

class Bus(Car):

    def __init__(self, horsepower, weight, engine_type, max_seats, busy_seats = 0):
        super().__init__(horsepower, weight, engine_type)
        self.busy_seats = busy_seats
        self.max_seats = max_seats

    def add_passenger(self):
        self.busy_seats += 1

    def free_seats(self):
        return self.max_seats - self.busy_seats

higer = Bus(250, 3000, "2.8L I4 turbo Diesel engine", 24 , 5)


higer.add_passenger()
print(higer.__dict__)
print(higer.free_seats())


# --------------------


# Research
# ---------------

"""
__dict__-y pahuma objecti atributnery u iranc arjeqnery
dir-y veradarcnuma mez objecti sax attributi anunery listi mej

"""




# ---------------
