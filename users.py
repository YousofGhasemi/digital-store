from store import Store, Product


class User:

    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"User with ({self.username}) username"


class Admin(User):
    def __init__(self, username):
        super().__init__(username)

    def add_product(self, store, product):
        if isinstance(store, Store) and isinstance(product, Product):
            store.add_product(product)
            print(f"Admin {self.username} added {product.name} to {store.name}")
        else:
            print("Invalid Store or Product!")

    def remove_product(self, store, product):
        if isinstance(store, Store) and isinstance(product, Product):
            store.remove_product(product)
            print(f"Admin {self.username} removed {product.name} from {store.name}")


class Customer(User):
    def __init__(self, username):
        super().__init__(username)
        self.cart = []

    def add_to_cart(self, product, count):
        if not isinstance(product, Product):
            print("Invalid product!")
        else:
            if count <= 0:
                print("Count must be positive!")
            else:
                repeted = False
                for i, item in enumerate(self.cart):
                    p, c = item
                    if p == product:
                        self.cart[i] = (p, c + count)
                        repeted = True
                        break
                if not repeted:
                    self.cart.append((product, count))

                print(f"{count} of {product} is added to cart!")

    def total_cart(self):
        total = 0
        for product, quantity in self.cart:
            if hasattr(product, "price"):
                total += product.price * quantity
        return total

    def checkout(self, payment_method):
        if not self.cart:
            print("Cart is empty!")
            return False

        total = self.total_cart()
        print(f"Total: {total} {Product.currency}")
        print(f"Payment method: {payment_method}")

        print("Checkout successful!")
        self.cart.clear()
        return True
