# Initializing Class variables using methods

class Bikes:

    def initialization_method(self,brand,model,price,mileage):
        self.brand = brand
        self.model = model
        self.price = price
        self.mileage = mileage
        
    def start_bike(self):
        print(self.brand+" bike having model as "+self.model+" has started")

    def stop_bike(self):
        print(self.brand+" bike having model as "+self.model+" has stopped")
        
    def print_bike_details(self):
        print("Brand of the bike is: "+self.brand)
        print("Model of the bike is: "+self.model)
        print("Price of the bike is: "+str(self.price))
        print("Mileage of the bike is: "+str(self.mileage))
        print("******************************************")
        

shine = Bikes()
shine.initialization_method('Honda','CB Shine',85000,54.5)
shine.start_bike()
shine.stop_bike()
shine.print_bike_details()

royal = Bikes()
royal.initialization_method("Royal Enfield","Interceptor",350000,20)
royal.start_bike()
royal.stop_bike()
royal.print_bike_details()

