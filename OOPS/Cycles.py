# using __init__ method

class Cycles:

    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def start_cycle(self):
        print(self.brand+" cycle having model as "+self.model+" has started.")

    def stop_car(self):
        print(self.brand+" cycle having model as "+self.model+" has stopped.")

    def print_cycle_details(self):
        print("Brand of the cycle: "+self.brand)
        print("Model of the cycle: "+self.model)
        print("Price of the cycle: "+str(self.price))
        print("************************************")


hero = Cycles("Hero","Ranger",12000)
atlas = Cycles("Atlas","Racer",16000)

hero.start_cycle()
hero.stop_car()
hero.print_cycle_details()

atlas.start_cycle()
atlas.stop_car()
atlas.print_cycle_details()

