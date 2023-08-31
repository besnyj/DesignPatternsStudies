def typesAndPrices(function):
    def wrapper():
        print("0. Espresso - $10\n1. Cappuccino - $5\n2. Latte\n3. Affogato - $15")
        return function()
    return wrapper

def addOnTypesAndPrices(function):
    def wrapper():
        print("0. Milk - $2\n1. Sugar $1")
        return function()
    return wrapper