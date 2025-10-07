class Store:
    pass


class Order:
    pass


class Product:
    currency = "IRR"

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"A {self.name} Product priced at {self.price} {self.currency} and with a stock of {self.stock}"

    def add_stock(self, Amount):
        Amount = int(Amount)
        if Amount > 0:
            new_stock = self.stock + Amount
            self.stock = new_stock
            print(
                f"The quantity of {Amount} units has been added to the inventory of {self.name} products and the new inventory is equal to {new_stock} units."
            )
            return new_stock
        else:
            print("Add some more!!!")
            return False

    def reduce_stock(self, Amount):
        Amount = int(Amount)
        if Amount <= self.stock:
            new_stock = self.stock - Amount
            self.stock = new_stock
            print(
                f"The quantity of {Amount} units is deducted from the inventory of {self.name} products and the new inventory is equal to {new_stock} units."
            )
            return new_stock
        else:
            print("Not enough inventory!!!")
            return False
