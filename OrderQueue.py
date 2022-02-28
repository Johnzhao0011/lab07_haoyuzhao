from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder

class OrderQueue:
    def __init__(self):
        self.minHeap = [0]
        self.currentSize = 0

    def percUp(self,i):
        while i // 2 > 0:
            if self.minHeap[i].getTime() < self.minHeap[i // 2].getTime():
                tmp = self.minHeap[i // 2]
                self.minHeap[i // 2] = self.minHeap[i]
                self.minHeap[i] = tmp
            i = i // 2

    def addOrder(self,pizzaOrder):
            self.minHeap.append(pizzaOrder)
            self.currentSize = self.currentSize + 1
            self.percUp(self.currentSize)

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.minHeap[i].getTime() > self.minHeap[mc].getTime():
                tmp = self.minHeap[i]
                self.minHeap[i] = self.minHeap[mc]
                self.minHeap[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.minHeap[i*2].getTime() < self.minHeap[i*2+1].getTime():
                return i * 2
            else:
                return i * 2 + 1

    def processNextOrder(self):
        if len(self.minHeap) == 1:
            raise QueueEmptyException()
        retval = self.minHeap[1].getOrderDescription()
        self.minHeap[1] = self.minHeap[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.minHeap.pop()
        self.percDown(1)
        return retval

class QueueEmptyException(Exception):
    pass
    
