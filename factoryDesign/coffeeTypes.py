from abc import ABC, abstractstaticmethod


class ICoffee(ABC):
    
    @abstractstaticmethod
    def coffeeRecipe(self):
        pass
    
    
class Espresso(ICoffee):
    
    def __init__(self, price):
        self.price = price
        self.name = "Espresso"
    
    def coffeeRecipe(self):
            return "100ml of water and 10g of coffee"
          

class Cappuccino(ICoffee):
    
    def __init__(self, price):
        self.price = price
        self.name = "Cappuccino"
    
    def coffeeRecipe(self):
        return "400ml of water and 50g of coffee"


class Latte(ICoffee):
    
    def __init__(self, price):
        self.price = price
        self.name = "Latte"        
    
    def coffeeRecipe(self):
        return "200ml of water and 50g of coffee"


class Affogato(ICoffee):

    def __init__(self, price):
        self.price = price
        self.name = "Affogato"
    
    def coffeeRecipe(self):
        return "150ml of water and 30g of coffee"
   
    
coffeeDict = {
    "0":Espresso(10),
    "1":Cappuccino(5),
    "2":Latte(3),
    "3":Affogato(15)
}
   
    
class CoffeeFactory:
    
    @staticmethod
    def selectCoffee(coffeeIndex):
        return coffeeDict[coffeeIndex]
