class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"Drive the car {self.model}")

    def stop(self):
        print(f"Stop the car {self.model}")

    def describe_car(self):
        print(f"{self.model} {self.year} {self.color}")


car1 = Car("Range Rover", 2025, "Black", False)
car2 = Car("BMW", 2020,"Blue", False)
print(car1.model, car1.year, car1.color, car1.for_sale)
# Function call
car1.describe_car()
car2.stop()

