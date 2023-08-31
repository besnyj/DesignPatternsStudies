from decorators import typesAndPrices, addOnTypesAndPrices
from coffeeTypes import CoffeeFactory
from addOns import AddOnFactory


print("welcome to Donald Trump's coffee shop!!!")

@typesAndPrices
def coffeSelection():
    coffeeSelection = input("What type of coffee would you like to order?\n")
    coffeeSelection = CoffeeFactory.selectCoffee(coffeeSelection)
    return coffeeSelection


@addOnTypesAndPrices    
def addOnSelection():
    addOnSelection = input("What type of addons you want?\n")
    addOnSelection = AddOnFactory.selectAddOn(addOnSelection)
    return addOnSelection

coffee = coffeSelection()
addOn = addOnSelection()

print(f'You ordered a {coffee.name} with {addOn.name} for a total of ${coffee.price + addOn.price}!')