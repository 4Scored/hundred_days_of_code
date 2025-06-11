# args | kwaargs

# *args - accepts any number of arguments

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3,5,6,9,2,1,9,30))


# **kwargs - unlimited keyword arguments

def calc(**kwargs):
    sum = 0
    sum += kwargs["add"]
    sum *= kwargs["multiply"]
    return sum

print(calc(add=3, multiply=5))


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan")
print(my_car.model)
