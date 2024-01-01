# Function - Function outside the class is known as Function.
def sample_function():
    print("Inside sample function.")


class Cars:
    wheels = 4

    # Method - Function inside the class is known as Method.
    def start_car(self):  # self keyword for inside the class functions
        print("Car started.")

    def stop_car(self):
        print("Car stopped.")

    def sample_one(self,brand,model,price,mileage):
        print(brand,model,price,mileage)

    def sample_two(self):
        print(self.wheels)

    def sample_three(self,brand,model,price,mileage):
        # to access properties of method outside the method
        # by creating class variables - we can access
        self.brand = brand
        self.model = model
        self.price = price
        self.mileage = mileage
        print(brand,model,price,mileage)

    def sample_four(self):
        print(self.wheels)
        # we can access the other method variables outside the method
        print(self.brand,self.model,self.price,self.mileage)
        self.start_car()


# Object creation statement by using Class name
obj = Cars()
# to refer this by using a variable name - 'obj' - object reference

# we can access the variables and methods by using the object reference
print(obj.wheels)
obj.start_car()
sample_function()  # we can call using function name when it is outside the class

# we can create any number of object references for a class
print("Honda Brio.")
brio = Cars()
brio.start_car()


new_obj = Cars()
new_obj.sample_one("Honda","Brio",800000,19.5)
new_obj.sample_two()
new_obj.sample_three("Maruti","Swift",900000,17)
new_obj.sample_four()