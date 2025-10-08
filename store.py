class Store:

    def __init__(self, name):
        self.name = name
        self.products = []
        self.orders = []

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

    def show_orders(self):
        if not self.orders:
            print(f"No orders in {self.name}")
        else:
            for i, order in enumerate(self.orders, start=1):
                print(f"{i}. {order}")

    def list_products(self):
        if self.products:
            for prod in self.products:
                print(prod)
        else:
            print(f"there is no product in {self.name}")


class Product:
    currency = "IRR"

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - {self.price} {self.currency} (Stock: {self.stock})"

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, stock={self.stock})"

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
            self.stock -= Amount
            print(
                f"The quantity of {Amount} units is deducted from the inventory of {self.name} products and the new inventory is equal to {self.stock} units."
            )
            return self.stock
        else:
            print("Not enough inventory!!!")
            return False
