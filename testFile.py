from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue

def test_Pizza():
    cp1 = Pizza("S")
    assert cp1.getPrice() == 0.0
    assert cp1.getSize() == "S"
    cp2 = cp1.setSize("M")
    assert cp1.getSize() == "M"


def test_CustomPizza():
    cp1 = CustomPizza("S")

    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n"

    cp2 = CustomPizza("L")
    cp2.addTopping("extra cheese")
    cp2.addTopping("sausage")

    assert cp2.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $14.00\n"


def test_SpecialtyPizza():
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"
    sp2 = SpecialtyPizza("L", "John Zhao")
    assert sp2.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: L\n\
Name: John Zhao\n\
Price: $16.00\n"
    
def test_PizzaOrder():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) 
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == \
"******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"

def test_OrderQueue():
    cp1 = CustomPizza("L")
    cp1.addTopping("Pineapple")
    cp1.addTopping("bacon")
    sp1 = SpecialtyPizza("S", "Carne-more")
    sp2 = SpecialtyPizza("L", "Leno")
    order1 = PizzaOrder(154030) 
    order1.addPizza(cp1)
    order2 = PizzaOrder(173030)
    order2.addPizza(sp1)
    order3 = PizzaOrder(140302)
    order3.addPizza(sp2)
    

    q1 = OrderQueue()
    q1.addOrder(order1)
    assert q1.currentSize == 1

    q1.addOrder(order2)
    assert q1.currentSize == 2
    
    q1.addOrder(order3)
    assert q1.currentSize == 3

    assert q1.minHeap == [0, order3, order1, order2]

    assert q1.processNextOrder() == order3.getOrderDescription()
    assert q1.currentSize == 2

    assert q1.processNextOrder() == order1.getOrderDescription()
    assert q1.currentSize == 1

    assert q1.processNextOrder() == order2.getOrderDescription()
    assert q1.currentSize == 0
