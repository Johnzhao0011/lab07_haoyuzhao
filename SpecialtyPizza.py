from Pizza import Pizza
from CustomPizza import CustomPizza

class SpecialtyPizza(Pizza):

    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
        if self.size == 'S':
            self.price = 12.00
            
        if self.size == 'M':
            self.price = 14.00

        if self.size == 'L':
            self.price = 16.0

    

    def getPizzaDetails(self):
        s = "SPECIALTY PIZZA\nSize: {}\nName: {}\nPrice: ${:.2f}\n".format(self.size, self.name, self.price)
        return s
