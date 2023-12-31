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

