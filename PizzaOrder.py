from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder():
    
    def __init__(self,time):
        self.time = time
        self.pizzas = []

    def getTime(self):
        return self.time

    def setTime(self,time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        totalprice = 0.00
        for i in self.pizzas:
            totalprice += i.getPrice()

        order = '******\nOrder Time: {}\n'.format(self.getTime())
        for item in self.pizzas:
            order = order + '{}'.format(item.getPizzaDetails()) + '\n----\n'
        order = order + 'TOTAL ORDER PRICE: ${:.2f}\n'.format(totalprice)
        order = order + '******\n'
        return order
        
        
