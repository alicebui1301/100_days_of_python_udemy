class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.year = kw.get("year")
        self.color = kw.get("color")
        self.seats = kw.get("seats")   
        
my_car = Car(make="Nissan", model="GT-R", year=2021)
print(my_car.make)
print(my_car.model)