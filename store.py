class Store:

    def __init__(self, name):
        self.name = name
        self.products = []

    def __str__(self):
        return f"{self.name} Store"

    def __len__(self):
        return len(self.products)

    def add_product(self, product):
        self.products.append(product)
        print(f"the {product.name} has been added to the {self.name}")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"the {product.name} has been removed from {self.name}")
        else:
            print(f"the {product.name} is not in {self.name}")

    def list_product(self):
        if self.products:
            for prod in self.products:
                print(prod)
        else:
            print(f"there is no product in {self.name}")


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
