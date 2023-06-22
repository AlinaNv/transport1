class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def ur(self):
        print (f'Name: {self.name}, Speed:{self.max_speed}, Mileage:{self.mileage}')

Autobus=Transport('Renault Logan', 180, 12)
Autobus.ur()


