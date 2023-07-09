# Create a class with attributes
class Car1:
    max_speed = 300
    mileage = 20

# Create a class with instance attributes
class Car2:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

m1 = Car1()
m2 = Car2(300, 20)

m1.max_speed
# 300
m2.max_speed
# 300

# Create a class with no attributes and methods
class Car3:
    pass

# Create a child class that will inherit all of the attributes and methods of the parent class
class Car:
    def __init__(self, brand, max_speed, mileage):
        self.brand = brand
        self.max_speed = max_speed
        self.mileage = mileage

class Tesla(Car):
    pass
m4 = Tesla("Tesla", 360, 30)
print ("Car brand: {}, Maximum speed: {}, Mileage: {}.".format(m4.brand, m4.max_speed, m4.mileage))

# Create a class with attributes and method 
class Car:
    def __init__(self, brand, max_speed, mileage):
        self.brand = brand
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seat_capacity(self, capacity):
        return "The seating capacity of a {} is {} passengers".format(self.brand, capacity)
m5 = Car("Audi", 350, 30)
m5.seat_capacity(5)
# 'The seating capacity of a Audi is 5 passengers'

# Create a child class that will inherit all of the attributes and methods (default value of capacity: 3) of the parent class
class MINI(Car):
    def seat_capacity(self, capacity=3):
        return super().seat_capacity(capacity=3) # super() access methods of the base class
m5 = MINI("MINI", 250, 15)
m5.seat_capacity()

# Instance variable vs class variable
class Car:
    def __init__(self, brand, max_speed, mileage, color = "White"):
        self.brand = brand
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

class Tesla(Car):
    pass

m6 = Tesla("Tesla Model Y", 155, 330)
m6_2 = Tesla("Tesla Model S", 200, 405)
m6.color
m6_2.color
# Variables created in .__init__() are called instance variables. 
# # An instance variable’s value is specific to a particular instance of the class. 
# For example, all car objects have a name and a max_speed, but the name and max_speed variables’ values will vary depending on the car instance.

# Define a color attribute that must have the same value for every class instance
class Car:
    color = "White"
    def __init__(self, brand, max_speed, mileage):
        self.brand = brand
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

class Tesla(Car):
    pass

m7 = Tesla("Tesla Model Y", 155, 330)
m7.color
# The class variable is shared between all class instances. 
# We can define a class attribute by assigning a value to a variable name outside of .__init__().
