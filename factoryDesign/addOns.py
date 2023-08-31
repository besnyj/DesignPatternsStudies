from abc import ABC, abstractstaticmethod

class IAddOns(ABC):
    
    @abstractstaticmethod
    def addOnPrice():
        pass
    
class Milk(IAddOns):
    
    def __init__(self, price):
        self.price = price
        self.name = "Milk"
    
    def addOnPrice(self):
        return self.price
    
class Sugar(IAddOns):
    
    def __init__(self, price):
        self.price = price
        self.name = "Sugar"
    
    def addOnPrice(self):
        return self.price
    
    
addOnDict = {
    "0": Milk(2),
    "1": Sugar(1)
}

class AddOnFactory:
    
    @staticmethod
    def selectAddOn(addOnIndex):
        return addOnDict[addOnIndex]