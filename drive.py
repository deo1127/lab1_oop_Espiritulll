class Car:
    wheels = 4  

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0  

    
    def drive(self, km):
        if km > 0:
            self.mileage += km
            print(f"Drove {km} km. Total mileage: {self.mileage} km")
        else:
            print("Distance must be a positive number!")

   
    def age(self, current_year):
        return current_year - self.year

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} - Wheels: {self.wheels} -Mileage: {self.mileage} km"

car1 = Car("Toyota", "Fortuner", 2024)
car2 = Car("Toyota", "Vios", 2024)
car3 = Car("Ford", "Ranger", 2025)

print(car1)
car1.drive(100)
car1.drive(-50)
    
print(f"Car 1 age in 2026: {car1.age(2026)} years")
    
print("\n" + str(car2))
print(car3)