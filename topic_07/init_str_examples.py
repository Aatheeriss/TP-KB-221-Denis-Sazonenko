class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.manufacturer} {self.model}"

my_car = Car("Hyondai", "Tucson", 2008)

print(my_car) 