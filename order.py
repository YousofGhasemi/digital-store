from datetime import datetime
import uuid
import store


class Order:

    def __init__(self, customer, items, total_amount):
        self.customer = customer
        self.status = "Pending"
        self.items = items
        self.total_amount = total_amount
        self.order_id = str(uuid.uuid4())[:8]
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"Order {self.order_id} by {self.customer.username} - {self.total_amount} IRR ({self.status})"

    def calculate_total(self):
        pass

    def mark_as_paid(self):
        pass
