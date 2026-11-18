class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        

    def __str__(self):
        return f"{self.brand} {self.model} {self.year} - Wheels: {self.wheels}"

car1 = Car("BMW", "3 series", 2025)
car2 = Car("Ford", "Mustang", 2025)
car3 = Car("Hyundai", "Elantra", 2025)

print(car1)
print(car2)
print(car3)