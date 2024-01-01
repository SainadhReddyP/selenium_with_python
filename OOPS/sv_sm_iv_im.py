# Static variables, Static methods, Instance variables, Instance methods

class Car:

    wheels = 4

    def __init__(self,brand,model,price,mileage):
        # instance variable
        self.brand = brand
        self.model = model
        self.price = price
        self.mileage = mileage

    def start_car(self):
        # instance method
        print(self.brand+" having model as "+self.model+" has started.")

    def stop_car(self):
        # instance method
        print(self.brand+" having model as "+self.model+" has stopped.")

    @staticmethod
    def print_car_wheels():  # self is not required for static methods
        print(Car.wheels)  # In static methods we can access static variables by using class name


# variables changing object to object is called instance variables
brio = Car("Honda","Brio",800000,19.5)
brio.start_car()
brio.stop_car()
Car.print_car_wheels()  # we can access static method using class name

# variables changing object to object is called instance variables
swift = Car("Maruti","Swift",900000,17)
swift.start_car()
swift.stop_car()
Car.print_car_wheels()


