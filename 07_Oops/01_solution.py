
# basic class and object
class Car:
	car_count = 0
	def __init__(self, brand , model):
		self.__brand = brand
		self.__model = model
		Car.car_count += 1

	def fullName(self):
		return f"the Car is : {self.__brand} {self.__model}"
	def get_brand(self):
		return self.__brand
	def fuel_type(self):
		return "Petrol"
	
	@staticmethod
	def car_description(self):
		return f"The {self.__model} is a {self.fuel_type()} car"
	
	@property
	def model(self):
		return self.__model

class ElectricCar(Car):
	def __init__(self, brand, model, batterySize):
		super().__init__(brand, model)
		self.batterySize = batterySize

	def fuel_type(self):
		return "Electricity"


new_car = Car("Honda", "Civic")
eletric_car = ElectricCar("Tesla", "Model 3", "60 KWh")
eletric_car_2 = ElectricCar("electric car 2", "Model 3", "80 KWh")

# print(new_car.get_brand(), new_car.model)
# print(new_car.fullName())
# print(Car.get_brand(new_car))

# print(new_car.fuel_type())
# print(eletric_car.fuel_type())

# print(Car.car_count)
# print(Car.car_description(new_car))

# print(new_car.model)

# print(isinstance(eletric_car, ElectricCar))
# print(isinstance(new_car, Car))

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
	def car_type(self):
		return "This is Electric Car"

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
print(my_new_tesla.car_type())
