from Pizza import Pizza

class CustomPizza(Pizza):
    
    def __init__(self, size):
        super().__init__(size)
        self.toppinglist = []
        if self.size == 'S':
            self.price = 8.00
            
        if self.size == 'M':
            self.price = 10.00

        if self.size == 'L':
            self.price = 12.00
        


    def addTopping(self, topping):
        self.topping = topping
        self.toppinglist.append(topping)
       
        if self.size == 'S':
            self.price += 0.50

        if self.size == 'M':
            self.price += 0.75

        if self.size == 'L':
            self.price += 1.00

    def getPizzaDetails(self):
        toppinglist = ''
        for item in self.toppinglist:
            toppinglist += "\t+ {}\n".format(item)
        s = "CUSTOM PIZZA\nSize: {}\nToppings:\n{}Price: ${:.2f}\n".format(self.size, toppinglist, self.price)
        return s

