from store import Store, Product


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return f"User: {self.username} ({self.email})"


class Admin(User):
    def __init__(self, username, password, email):
        super().__init__(username, password, email)

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
    def __init__(self, username, password, email):
        super().__init__(username, password, email)
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

    def remove_from_cart(self, product, count):
        if not isinstance(product, Product):
            print("Invalid product!")
        else:
            if count <= 0:
                print("Count must be positive!")
            else:
                for i, item in enumerate(self.cart):
                    p, c = item
                    if p == product:
                        new_count = c - count
                        if new_count <= 0:
                            self.cart.pop(i)
                            print(f"{product.name} removed from cart.")
                        else:
                            self.cart[i] = (p, new_count)
                            print(
                                f"{count} of {product.name} removed. Remaining: {new_count}"
                            )
                        break

    def show_cart(self):
        for i, item in enumerate(self.cart):
            product, count = self.cart[i]
            print(f"{i+1}- {product} : {count}")

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
        # payment method is in process!
        print("Checkout successful!")
        self.cart.clear()
        return True
